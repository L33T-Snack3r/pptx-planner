import google.genai as genai

class Gemini_LLM():
    def __init__(self, api_key : str, model : str ="gemini-1.5-flash", temperature=0):
        self.model = model
        self.temperature = temperature
        self.client = genai.Client(api_key=api_key)
        
    def call(self, query : str):
        response = self.client.models.generate_content(
            model=self.model,
            contents=query,
            config=genai.types.GenerateContentConfig(
                temperature=self.temperature
                )
        )

        output = {"text" : response.text,
                  "full_response": response}

        return output