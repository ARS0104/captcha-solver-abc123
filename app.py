from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Dummy secret for now — replace this later if you get a real one
EXPECTED_SECRET = "abc123"

@app.route('/api-endpoint', methods=['POST'])
def api_endpoint():
    data = request.get_json()

    # 🔐 Secret validation
    if not data or data.get("secret") != EXPECTED_SECRET:
        return jsonify({
            "status": "error",
            "message": "Invalid or missing secret"
        }), 401

    # 🧠 Parse important fields from the request
    email = data.get("email")
    task = data.get("task")
    round_number = data.get("round")
    nonce = data.get("nonce")
    brief = data.get("brief")
    evaluation_url = data.get("evaluation_url")
    attachments = data.get("attachments", [])

    # 🖨️ Log them for now
    print("✅ Valid Task Received:")
    print(f"Email: {email}")
    print(f"Task: {task}")
    print(f"Round: {round_number}")
    print(f"Nonce: {nonce}")
    print(f"Brief: {brief}")
    print(f"Evaluation URL: {evaluation_url}")
    print(f"Attachments: {attachments}")

    return jsonify({
        "status": "success",
        "message": "Task received and parsed"
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
