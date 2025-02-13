from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        print("Received data:", data)

        character = data.get("character", "Unknown Character")
        user_message = data.get("user_message", "")

        print(f"Character: {character}, User Message: {user_message}")

        response_text = f"{character} says: {user_message[::-1]}"

        return jsonify({"character": character, "response": response_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
