import requests
import json

class OllamaClient:
    def __init__(self, host="http://localhost:11434", model=None):
        self.host = host
        self.model = model
    
    def generate(self, prompt, model=None, stream=True):
        url = f"{self.host}/api/generate"
        data = {
            "model": model or self.model or "llama2",
            "prompt": prompt,
            "stream": stream
        }
        
        response = requests.post(url, json=data, stream=stream)
        response.raise_for_status()
        
        if stream:
            def stream_generator():
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line)
                        if "response" in chunk:
                            yield chunk["response"]
                        if chunk.get("done"):
                            break
            return stream_generator()
        else:
            return response.json().get("response", "")

# Test it
if __name__ == "__main__":
    client = OllamaClient(model="smollm2:latest")
    
    print("Testing Ollama client...")
    try:
        # Quick test
        result = client.generate("Say hello", stream=False)
        print(f"Response: {result}")
        
        # Streaming test
        print("\nStreaming test:")
        for chunk in client.generate("Count to 3"):
            print(chunk, end="", flush=True)
        print("\nDone!")
        
    except Exception as e:
        print(f"Error: {e}")
