import io
import base64
from typing import List
from openai import OpenAI
from PIL import Image

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
    
    def call_with_images(self, query : str, images : List[Image.Image] | Image.Image):
        images_list = [images] if isinstance(images, Image.Image) else images

        payload = [{"type" : "input_image", 
                    "image_url" : self.image_to_base64(img)} 
                    for img in images_list]
        
        payload = [{"type" : "input_text", "text" : query}] + payload

        response = self.client.responses.create(
            model=self.model,
            input=[{
                    "role" : "user",
                    "content" : payload
                   }],
            temperature=self.temperature
        )

        output = {"text" : response.output[0].content[0].text,
                  "full_response": response}
        
        return output

    def image_to_base64(self, img: Image.Image, format: str = "JPEG") -> str:

        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        # Encode the bytes to base64
        encoded_string = base64.b64encode(img_byte_arr).decode('utf-8')

        # Construct the data URI
        # OpenAI requires this format for inline images
        return f"data:image/{format.lower()};base64,{encoded_string}"