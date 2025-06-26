import os
from dotenv import load_dotenv
from llm.gemini import Gemini_LLM
from llm.openai import OpenAI_LLM
from typing import List
from PIL import Image
import logging 

logging.basicConfig(level=logging.INFO)
load_dotenv('../local.env')

class LLM():
    def __init__(self, provider : str, model : str = None, temperature=0):

        api_key = os.getenv(f"{provider.upper()}_API_KEY")
        if not api_key:
            raise Exception(f"{provider.upper()}_API_KEY not found in env variable file")

        if provider == "gemini":
            self.llm = Gemini_LLM(api_key=os.getenv(api_key), model=model, temperature=temperature) if model else \
                       Gemini_LLM(api_key=os.getenv(api_key), temperature=temperature)
        elif provider == "openai":
            self.llm = OpenAI_LLM(api_key=os.getenv(api_key), model=model, temperature=temperature) if model else \
                       OpenAI_LLM(api_key=os.getenv(api_key), temperature=temperature)
        else:
            raise Exception(f"{provider} is not supported")
        
        logging.info("LLM initialized")
        logging.info(f"Provider: {provider}")
        logging.info(f"Model: {self.llm.model}")
    
    def call(self, query : str):
        return self.llm.call(query)
    
    def call_with_images(self, query : str, images : List[Image.Image] | Image.Image):
        return self.llm.call_with_images(query, images)