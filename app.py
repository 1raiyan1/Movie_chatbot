from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import redis
import hashlib
import time
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from celery import Celery

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379, db=0)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per second"]
)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
model_name = "facebook/opt-1.3b"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)


def generate_cache_key(user_input):
    """Generate a hash key for caching responses"""
    return hashlib.sha256(user_input.encode()).hexdigest()


@celery.task
def generate_response_task(prompt):
    """Asynchronous task for generating a response"""
    response = generator(
        prompt,
        max_length=100,
        num_return_sequences=1,
        truncation=True,
        pad_token_id=tokenizer.eos_token_id
    )
    return response[0]["generated_text"].replace(prompt, "").strip()


@app.route("/")
def home():
    return "Chatbot is running!"


@app.route("/chat", methods=["GET"])
@limiter.limit("5 per second") 
def chat():
    user_input = request.args.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    cache_key = generate_cache_key(user_input)
    cached_response = redis_client.get(cache_key)
    if cached_response:
        return jsonify({"response": cached_response.decode()}), 200

    prompt = f"User: {user_input}\nAI:"
    response = generate_response_task(prompt)
    redis_client.setex(cache_key, 60, response)

    return jsonify({"response": response}), 200


if __name__ == "__main__":
    app.run(debug=False)