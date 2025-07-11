# OSpitter

OSpitter is a modern, full-stack web client for interacting with local Ollama models. It features a beautiful chat interface, Markdown and LaTeX rendering, code highlighting, streaming/non-streaming support, and a fun spitting llama theme.

## Features

- **Chat with Ollama models**: Send prompts and receive AI-generated responses.
- **Streaming & Non-Streaming**: Choose between real-time streaming or full-response modes.
- **Markdown & LaTeX Support**: Render Markdown and math formulas in responses.
- **Code Syntax Highlighting**: Beautifully formatted code blocks.
- **SVG & Web Content Rendering**: Supports SVG and web content in responses.
- **Conversation Turn Limit**: Prevent runaway sessions (default: 20 turns).
- **Stop Button**: Interrupt generation at any time.
- **Sticky Input Area**: Input stays visible as chat grows.
- **Mobile Responsive**: Works well on desktop and mobile.
- **Fun Branding**: Spitting llama logo and playful theme.

## Screenshots

![OSpitter UI](docs/osplitter-screenshot.png) <!-- Add screenshot if available -->

## Getting Started

### Prerequisites
- Python 3.8+
- Ollama installed and running locally
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ospitter.git
   cd ospitter
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Start the Flask server**
   ```bash
   python app.py
   ```
   The app will run on `http://localhost:5000` by default.

### Configuration
- **Model Selection**: Choose from available models in the dropdown (e.g., `smollm2:latest`, `llama2`, `codellama`).
- **Turn Limit**: Default is 20 turns per session. Change `TURN_LIMIT` in app.py to adjust.

## Usage

- Open your browser and go to `http://localhost:5000`.
- Type your prompt and select a model.
- Use the stop button to interrupt long generations.
- Enjoy Markdown, LaTeX, and code rendering in responses.

## Project Structure

```
app.py                  # Flask backend
ollama_client.py        # Ollama API client
requirements.txt        # Python dependencies
/templates/index.html   # Frontend UI
/static/                # (Optional) Static assets
```

## Customization
- **Branding**: Edit index.html to change logo, colors, or layout.
- **Models**: Update `/api/models` endpoint in app.py to list your installed models.
- **Frontend Libraries**: Uses CDN for marked.js, KaTeX, and highlight.js.

## Troubleshooting
- **Ollama not responding**: Ensure Ollama is running locally and models are available.
- **Streaming issues**: Some browsers may handle streaming differently; use non-streaming mode if needed.
- **Session expired**: Refresh the page to start a new session if turn limit is reached.

## License
MIT License

## Credits
- Llama emoji: Unicode
- SVG logo: Custom
- Built with Flask, marked.js, KaTeX, highlight.js

---

Enjoy chatting with your local AI llama!