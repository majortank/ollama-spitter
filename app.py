from flask import Flask, render_template, request, jsonify, Response, session
import json
from ollama_client import OllamaClient

app = Flask(__name__)
app.secret_key = 'ollama_secret_key'  # Needed for session management
client = OllamaClient(model="smollm2:latest")

# Conversation turn limit
TURN_LIMIT = 20

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    stream = data.get('stream', True)
    model = data.get('model', 'smollm2:latest')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Conversation turn limit logic
    if 'turns' not in session:
        session['turns'] = 0
    session['turns'] += 1
    if session['turns'] > TURN_LIMIT:
        return jsonify({'error': f'Conversation turn limit reached ({TURN_LIMIT}). Please refresh to start a new session.'}), 429

    try:
        if stream:
            def generate_stream():
                try:
                    for chunk in client.generate(prompt, model=model, stream=True):
                        yield f"data: {json.dumps({'chunk': chunk})}\n\n"
                        # Detect client disconnect (works in dev server)
                        if request.environ.get('werkzeug.server.shutdown') is not None:
                            break
                except (GeneratorExit, ConnectionError):
                    # Client disconnected, stop streaming
                    return
                except Exception as e:
                    yield f"data: {json.dumps({'error': str(e)})}\n\n"
                yield f"data: {json.dumps({'done': True})}\n\n"
            return Response(generate_stream(), mimetype='text/plain')
        else:
            response = client.generate(prompt, model=model, stream=False)
            return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/models')
def get_models():
    # You can expand this to actually fetch available models
    return jsonify(['smollm2:latest', 'llama2', 'codellama'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
