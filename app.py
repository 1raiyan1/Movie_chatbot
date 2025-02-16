from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

app = Flask(__name__)
model_name = "facebook/opt-1.3b"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.route("/")
def home():
    return "Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history

    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_input = data["message"]
    chat_history.append(f"User: {user_input}")
    chat_history = chat_history[-5:]

    prompt = "\n".join(chat_history) + "\nAI:"

    response = generator(
        prompt,
        max_length=50,
        num_return_sequences=1,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,
        truncation=True,
        pad_token_id=tokenizer.eos_token_id
    )

    generated_text = response[0]["generated_text"].split("AI:")[-1].strip()
    chat_history.append(f"AI: {generated_text}")

    return jsonify({"response": generated_text})

if __name__ == "__main__":
    app.run(debug=False)