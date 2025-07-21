
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