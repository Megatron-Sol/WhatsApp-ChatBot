# WhatsApp Flows Handler

This project is a Flask-based webhook handler for WhatsApp Flows. It responds to health checks, processes incoming requests, and ensures a smooth integration with Meta's WhatsApp API.

## Features
- Handles WhatsApp Flow webhooks.
- Responds to health check requests with a Base64-encoded payload.
- Runs on a local Flask server, exposed via ngrok.

## Prerequisites
Before running this project, make sure you have:
- Python 3 installed.
- Flask installed (`pip install flask`).
- ngrok installed (`https://ngrok.com/download`).

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/whatsapp-flows-handler.git
   cd whatsapp-flows-handler
   ```

## Running the Application
1. **Start the Flask server**:
   ```sh
   python app.py
   ```
   Ensure the output shows:
   ```
   Running on http://0.0.0.0:5000
   ```

2. **Expose the server with ngrok**:
   ```sh
   ngrok http 5000
   ```
   Copy the generated `https://your-ngrok-url.ngrok-free.app` and update your WhatsApp Flow webhook URL in Meta settings.

3. **Test the webhook manually**:
   ```sh
   curl -X POST https://your-ngrok-url.ngrok-free.app/webhook \
   -H "Content-Type: application/json" \
   -d '{"version": "3.0", "action": "ping"}'
   ```

   Expected response (Base64 encoded):
   ```json
   eyJkYXRhIjogeyJzdGF0dXMiOiAiYWN0aXZlIn19
   ```

## Troubleshooting
- If the webhook fails, check Flask logs for errors.
- Ensure that ngrok is running and forwarding requests to `localhost:5000`.
- If the response is not Base64-encoded, update `app.py` to return an encoded response.
