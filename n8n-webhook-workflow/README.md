# n8n Webhook Workflow

This project implements an n8n workflow that utilizes webhooks to handle incoming messages and respond accordingly. The workflow replaces the previous Ollama implementation with a more flexible webhook-based architecture.

## Project Structure

The project consists of the following files:

- `src/workflow.json`: Contains the main n8n workflow configuration, defining the nodes and their connections.
- `src/webhooks/receiveMessageWebhook.json`: Configuration for the webhook that receives messages, including settings for the webhook trigger node.
- `src/webhooks/respondMessageWebhook.json`: Configuration for the webhook that responds to messages, detailing how to format and send responses back to the user.

## Setup Instructions

1. **Install n8n**: Ensure you have n8n installed on your machine. You can follow the installation instructions on the [n8n documentation](https://docs.n8n.io/getting-started/installation/).

2. **Import the Workflow**:
   - Open n8n and navigate to the workflow editor.
   - Import the `src/workflow.json` file to load the main workflow configuration.

3. **Configure Webhooks**:
   - The `receiveMessageWebhook.json` file contains the configuration for the webhook that will receive incoming messages. Ensure that the HTTP method and endpoint are correctly set up to match your application's requirements.
   - The `respondMessageWebhook.json` file defines how to respond to messages. Adjust the response settings as needed to fit your use case.

4. **Testing**:
   - Once the workflow is set up, you can test the webhooks by sending HTTP requests to the configured endpoints. Monitor the responses to ensure everything is functioning as expected.

5. **Deployment**:
   - After testing, deploy your n8n instance to a production environment if necessary. Ensure that your webhooks are accessible from the internet if they need to handle external requests.

## Usage

This workflow is designed to facilitate message handling through webhooks, allowing for real-time interactions with users. Customize the workflow further based on your specific requirements and use cases.