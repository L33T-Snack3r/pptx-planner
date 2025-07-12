import google.genai as genai
from google.genai import types
from typing import List
from PIL import Image
import io

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

    def call_with_images(self, query : str, images : List[Image.Image] | Image.Image, thinking):
        images_list = [images] if isinstance(images, Image.Image) else images

        #Convert pillow image to byte array then wrap in typing
        payload = [types.Part.from_bytes(data=self.image_to_byte_array(img), \
                                         mime_type="image/jpeg") \
                    for img in images_list]

        payload = [query] + payload

        response = self.client.models.generate_content(
            model=self.model,
            contents=payload,
            config=genai.types.GenerateContentConfig(
                temperature=self.temperature,
                thinking_config=types.ThinkingConfig(thinking_budget=thinking)
                )
        )

        output = {"text" : response.text,
                  "full_response": response}
        
        return output

    def image_to_byte_array(self, img : Image.Image) -> bytes:
        img_byte_arr = io.BytesIO()
        if img.mode in ("RGBA", "P"): 
            img = img.convert("RGB")

        img.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        return img_byte_arr