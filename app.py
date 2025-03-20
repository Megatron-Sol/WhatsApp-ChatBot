import base64
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "WhatsApp Flow Handler is Running!", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received WhatsApp data:", data)

    # Handle health check request
    if data and data.get("action") == "ping":
        response_data = {"data": {"status": "active"}}
        json_response = json.dumps(response_data)
        encoded_response = base64.b64encode(json_response.encode()).decode()
        
        return encoded_response, 200, {"Content-Type": "text/plain"}

    # Process other messages or flows
    return jsonify({"status": "success"}), 200

@app.route("/webhook", methods=["GET"])
def verify():
    """Verify webhook with WhatsApp API"""
    token = "12345"  # Change this
    challenge = request.args.get("hub.challenge")
    verify_token = request.args.get("hub.verify_token")

    if verify_token == token:
        return challenge, 200
    return "Invalid verification token", 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
