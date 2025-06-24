from openai import OpenAI

class OpenAI_LLM():
    def __init__(self, api_key : str, model : str ="gpt-4o-mini", temperature=0):
        self.model = model
        self.temperature = temperature
        self.client = OpenAI(api_key=api_key)

    def call(self, query : str):
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[
                {
                    "role": "user",
                    "content": query,
                },
            ],
        )

        output = {"text" : response.choices[0].message.content,
                  "full_response": response}

        return output