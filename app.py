from flask import Flask, request, jsonify
from chatbot_api import ChatGPTBotAPI

OPEN_AI_API_KEY = "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"
app = Flask(__name__)

# Initialize the ChatGPTBotAPI instance
chatbot_api = ChatGPTBotAPI(OPEN_AI_API_KEY)

# Endpoint to create a new prompt
@app.route('/create_prompt', methods=['POST'])
def create_prompt():
    data = request.json
    prompt = data.get('prompt')
    indexPrompt = chatbot_api.create_prompt(prompt)
    return jsonify({"message": f"Prompt created successfully at index = {indexPrompt}"})

# Endpoint to get a response for a prompt
@app.route('/get_response/<int:index>', methods=['GET'])
def get_response(index):
    response = chatbot_api.get_response(index)
    return jsonify({"response": response})

# Endpoint to update an existing prompt
@app.route('/update_prompt/<int:index>', methods=['PUT'])
def update_prompt(index):
    data = request.json
    new_prompt = data.get('new_prompt')
    chatbot_api.update_prompt(index, new_prompt)
    return jsonify({"message": "Prompt updated successfully"})

# Endpoint to delete a prompt
@app.route('/delete_prompt/<int:index>', methods=['DELETE'])
def delete_prompt(index):
    chatbot_api.delete_prompt(index)
    return jsonify({"message": "Prompt deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
