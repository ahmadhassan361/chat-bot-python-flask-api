import openai

class ChatGPTBotAPI:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key
        self.prompts = []

    def create_prompt(self, prompt):
        self.prompts.append(prompt)
        return len(self.prompts) - 1  

    def get_response(self, prompt_index):
        if 0 <= prompt_index < len(self.prompts):
            prompt = self.prompts[prompt_index]
            messages = [{"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}]
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
            )
            return {'prompt':prompt,'result':response.choices[0].message["content"]}
        else:
            return "Prompt index out of range"

    def update_prompt(self, prompt_index, new_prompt):
        if 0 <= prompt_index < len(self.prompts):
            self.prompts[prompt_index] = new_prompt
            return "Prompt updated successfully"
        else:
            return "Prompt index out of range"

    def delete_prompt(self, prompt_index):
        if 0 <= prompt_index < len(self.prompts):
            del self.prompts[prompt_index]
            return "Prompt deleted successfully"
        else:
            return "Prompt index out of range"



# # Example usage
# api_key = "your_openai_api_key"
# chatbot_api = ChatGPTBotAPI(api_key)

# index = chatbot_api.create_prompt("Tell me a joke")
# response = chatbot_api.get_response(index)
# print(response)

# chatbot_api.update_prompt(index, "Tell me an interesting fact")
# response = chatbot_api.get_response(index)
# print(response)

# chatbot_api.delete_prompt(index)
