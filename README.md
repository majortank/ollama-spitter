
# OSpitter + n8n Webhook Integration

This project combines a Flask-based chat client for local Ollama models (OSpitter) with an n8n workflow for flexible automation and external integrations using webhooks.

## Project Structure

```
ollama-spitter/
├── app.py                  # Flask backend for OSpitter
├── ollama_client.py        # Ollama API client
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend UI for OSpitter
├── n8n-webhook-workflow/
│   ├── src/
│   │   ├── workflow.json   # Main n8n workflow (Webhook → Agent → Respond)
│   │   └── webhooks/
│   │       ├── receiveMessageWebhook.json # Webhook trigger node config
│   │       └── respondMessageWebhook.json # Webhook response node config
│   └── README.md           # n8n workflow documentation
└── README.md               # Main project documentation
```

## OSpitter (Flask App)

- **Purpose:** Chat with local Ollama models using a modern web UI.
- **Features:**
  - Markdown, LaTeX, code highlighting
  - Streaming and non-streaming responses
  - Conversation turn limit
  - Fun llama branding
- **API Endpoint:**
  - `POST /api/generate` — Send `{ "prompt": "...", "model": "...", "stream": true|false }`
  - Example: `curl -X POST http://192.168.110.90:5000/api/generate -H "Content-Type: application/json" -d '{"prompt":"Hello!","model":"smollm2:latest","stream":false}'`
- **Configuration:**
  - Host: `0.0.0.0` (accessible on local network)
  - Default port: `5000`

## n8n Webhook Workflow

- **Purpose:** Automate message handling and integrate with external systems using webhooks.
- **Main Workflow:**
  - Trigger: Webhook node (`/webhook/ecdd5670-8efa-462d-9694-c83178f14319`)
  - Processing: Agent node (guides user, processes input)
  - Response: Respond to Webhook node (returns result)
- **How to Trigger:**
  - Send a POST request to `https://n8n.tangikuu.space/webhook/ecdd5670-8efa-462d-9694-c83178f14319`
  - Example: `curl -X POST https://n8n.tangikuu.space/webhook/ecdd5670-8efa-462d-9694-c83178f14319 -H "Content-Type: application/json" -d '{"chatInput":"Hello!"}'`
- **Integration:**
  - n8n can send HTTP requests to OSpitter at `http://192.168.110.90:5000/api/generate` using an HTTP Request node.

## Setup Instructions

### OSpitter (Flask App)
1. Install Python 3.8+ and pip.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Flask server:
   ```bash
   python app.py
   ```
   The app will run on `http://192.168.110.90:5000`.

### n8n Workflow
1. Install n8n (see [n8n docs](https://docs.n8n.io/getting-started/installation/)).
2. Import `n8n-webhook-workflow/src/workflow.json` in the n8n editor.
3. Activate the workflow to enable webhooks.
4. Test by sending a POST request to the webhook URL.

## Troubleshooting
- **Webhook Error:** Ensure the n8n workflow is active and the webhook path matches.
- **Network Issues:** Make sure n8n can reach the Flask app at `192.168.110.90:5000` (check firewall and network settings).
- **Response Issues:** The Agent node should output its result in a field called `response` for the Respond node.

## Credits
- Built with Flask, n8n, and Ollama
- Llama emoji: Unicode
- SVG logo: Custom

---
Enjoy chatting with your local AI llama and automating with n8n!


## Testing

### 1. Testing OSpitter (Flask App)

- **Start the Flask server:**
  ```bash
  python app.py
  ```
  The app should be running at `http://192.168.110.90:5000`.

- **Test the API endpoint:**
  Send a POST request to `/api/generate`:
  ```bash
  curl -X POST http://192.168.110.90:5000/api/generate \
    -H "Content-Type: application/json" \
    -d '{"prompt":"Hello!","model":"smollm2:latest","stream":false}'
  ```
  - **Expected result:** JSON response with the AI-generated reply.
  - For streaming, set `"stream": true` and handle streamed output.

- **Web UI:**
  - Open `http://192.168.110.90:5000` in your browser.
  - Enter a prompt and select a model.
  - You should see responses rendered with Markdown, LaTeX, and code highlighting.

### 2. Testing n8n Webhook Workflow

- **Activate the workflow:**
  - In n8n, open the workflow and click "Activate".

- **Send a test webhook request:**
  ```bash
  curl -X POST https://n8n.tangikuu.space/webhook/ecdd5670-8efa-462d-9694-c83178f14319 \
    -H "Content-Type: application/json" \
    -d '{"chatInput":"Hello from n8n!"}'
  ```
  - **Expected result:** JSON response from the Agent node, returned by the Respond node.

- **Integration test:**
  - In n8n, add an HTTP Request node to send a POST to `http://192.168.110.90:5000/api/generate`.
  - Use the output from the webhook or Agent node as the prompt.
  - Confirm the response is received and passed through the workflow.

### 3. Troubleshooting

- **Webhook not triggering:**
  - Ensure the workflow is active in n8n.
  - Double-check the webhook path and method (POST).
  - Confirm n8n is reachable at `https://n8n.tangikuu.space`.

- **No response from Flask app:**
  - Make sure the Flask server is running and accessible from n8n.
  - Check firewall/network settings to allow traffic to `192.168.110.90:5000`.

- **Incorrect response format:**
  - The Agent node should output its result in a field called `response` for the Respond node.
  - Adjust the mapping in n8n if needed.

- **Session/turn limit reached:**
  - If you see a turn limit error, refresh the web UI or restart the session.

### 4. Example End-to-End Test

1. Start the Flask app and n8n workflow.
2. Send a POST to the n8n webhook URL with `{"chatInput":"Test integration"}`.
3. n8n processes the message, optionally sends it to OSpitter, and returns the AI response.
4. Check logs and responses for errors or unexpected results.

---
For advanced testing, use Postman or similar tools to automate requests and validate responses. Monitor logs in both Flask and n8n for debugging.