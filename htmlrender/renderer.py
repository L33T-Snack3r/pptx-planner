import os
from loguru import logger
from html2image import Html2Image
from PIL import Image, ImageFile

class HTMLRenderer():
    def __init__(self, size : tuple = (1440, 810)):
        self.hti = Html2Image(size=size)

    def renderHTML(self, html_str : str, tmp_filename : str = "html_render.png", resize : bool = False, resize_ratio : float = 0.5) -> ImageFile.ImageFile:
        image_path = self.hti.screenshot(html_str=html_str, save_as=tmp_filename)[0]
        logger.info(f"Saving rendered HTML image to temp file: {image_path}")

        pil_image = None
        try:
            # Use a context manager for Image.open to ensure the file handle is closed
            with Image.open(image_path) as img:
                img.load() # Load the image data into memory
                pil_image = img.copy() # Make a copy to decouple from the original file object
                                        # This is the most robust way to ensure the handle is released.
                                        # The 'with' block ensures 'img' is closed.

        finally:
            if os.path.exists(image_path):
                os.remove(image_path)
            logger.info(f"Temp file removed: {image_path}")
        
        if resize:
            pil_image = self.resize(pil_image, ratio=resize_ratio)

        return pil_image
        
    def resize(self, image : ImageFile.ImageFile, ratio : float) -> ImageFile.ImageFile:
        
        new_width, new_height =  int(float(image.size[0])*ratio), int(float(image.size[1])*ratio)

        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)