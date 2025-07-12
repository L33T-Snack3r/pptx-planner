from llm.llmwrapper import LLM
from PIL import Image
from htmlrender.renderer import HTMLRenderer
from utils.utils import find_text_in_between_tags
import textwrap
import time
from loguru import logger

class Generator():
    def __init__(self, render_resize_ratio=0.4):
        self.rndr = HTMLRenderer()
        self.render_resize_ratio = render_resize_ratio

    def reviewer(self, html_code : str, html_image : Image.Image, llm : LLM, custom_prompt : str = None)-> dict:
        slide_review_prompt = textwrap.dedent(
        """
        You are a senior front-end software engineer reviewing a junior engineer's work.
        He has written some HTML which is supposed to show one slide of a powerpoint.

        You have been provided with the HTML code and also a rendering of the code as an image.

        Look at the image then validate the following criteria.
        1. Make sure that text, visual elements and content blocks are completely contained within the slide and not cut off at the bottom of the slide. 
        If this criteria is not met, reduce the vertical padding/spacing between visual elements, titles, subtitles and content blocks OR reduce the font size of the text component to meet the criteria.
        You can reduce the padding by changing the padding or gap parameters, or the margin-bottom parameter of any titles.

        2. Make sure that visual elements do NOT overlap with each other e.g. the company logo overlaps with slide content.
        If anything is overlapping, MAKE SURE to reposition or adjust the size of the frontmost element.

        Do NOT make changes to the code if the above criteria is met.
        If code changes need to be made, only output the improved HTML code, do not output any other text.
        If the code meets all of the criteria, simply output <OK>.

        The HTML code is provided below:
        {code}
        """
        )

        if custom_prompt:
            slide_review_prompt = custom_prompt

        #Sanitizing input html
        html_code = find_text_in_between_tags(html_code, start_tag="<!DOCTYPE html>", end_tag="</html>", inclusive=True)

        review_prompt = slide_review_prompt.format(code=html_code)
        response = llm.call_with_images(query=review_prompt, images=[html_image])

        if '<OK>' in response['text']:
            return ({"status" : "unchanged", "html_code" : html_code})
        else:
            modified_html = find_text_in_between_tags(response['text'], start_tag="<!DOCTYPE html>", end_tag="</html>", inclusive=True)
            return ({"status" : "modified", "html_code" : modified_html})


    def generate_title_slide(self, query : str, slide_content : str, generator_llm : LLM, reviewer_llm : LLM, review : bool = True, custom_prompt : str = None) -> str:
        title_slide_prompt = textwrap.dedent(
        f"""
        You are a tech consultant, and you have been given the following request:

        "{query}"

        You are trying to create a set of slides for a proposal.
        The first slide you want to create is the title slide.
        Generate the title slide in HTML.

        Take into consideration the following points:
        - Choose a style that is both visually appealing and functional; befitting of a proposal from a top-tier tech consulting company.
        - What colour and design would be appropriate, especially for the background?
        - What font type should you use?
        - What should the size of the page be, to accurately reflect powerpoint slides? The slides must be 720p
        - The title font should be around 3.0em, and the subtitle around 1.8em, otherwise it is too big.
        - Make sure to include an empty footer e.g. 
            <div class="footer-bar w-full mt-auto relative">
                <div class="absolute bottom-2 right-4 text-white text-sm"></div>
            </div>
            
        This slide will become a template master slide which will define the style of the following slides, so design this slide with great care.
        Do not output any other text other than the html itself.
        If your slides are visually appealing but also functional, you will be rewarded with a bonus.

        The information that should be included on this slide is as follows:
        {slide_content}
        """
        )

        if custom_prompt:    
            title_slide_prompt = custom_prompt

        logger.info("Generating title slide...")
        html_code = \
            find_text_in_between_tags(generator_llm.call(query=title_slide_prompt)['text'], 
                                      start_tag="<!DOCTYPE html>", 
                                      end_tag="</html>", 
                                      inclusive=True)

        if review:
            logger.info("Reviewing generated HTML...")
            html_img = self.rndr.renderHTML(html_str=html_code, resize=True, resize_ratio=self.render_resize_ratio)
            review_response = self.reviewer(html_code, html_img, reviewer_llm)
            html_code = review_response['html_code']

        return html_code
    

    def generate_agenda_slide(self, query : str, slide_content : str, title_slide_html : str, generator_llm : LLM, reviewer_llm : LLM, review : bool = True, custom_prompt : str = None) -> str:
        agenda_slide_prompt = textwrap.dedent(
        f"""
        You are a tech consultant, and you have been given the following request:
        "{query}"

        You are trying to create a set of slides for a proposal.
        So far you have created the title slide, the html code for this slide is below.
        Next, you are creating the executive summary slide. Like the title slide, generate this slide in HTML.

        Title slide HTML:
        ```html
        {title_slide_html}
        ```

        Take into consideration the following points:
        - Make sure to follow a design style that matches the provided example HTML code to maintain consistency across the presentation.
        - DO NOT include the presenter name, their title, the date and any company logos on this slide. This is to save space.
        - Titles should be aligned to the top left-hand side of the slide
        - The font size, to make sure that text fits on the slide. 
        Titles should be 2.3em, subtitles at around 1.3em and normal text should be around 0.9em.
        If the slide content defined below is only a few key words or short sentences, you can increase the subtitle size up to 1.8, and normal text size up to 1.3.
        - Be creative with the slide design. Try your best to use visual elements to both enhance the message and make the slides visually engaging.
        - If you are displaying the slide content in a content grid, always set 
            grid-template-columns: auto auto;
            grid-template-rows: auto auto;
        - If relevant, use icons.
            
        This slide will become a template master slide which will define the style of the following slides, so design this slide with great care.
        Do not output any other text other than the html itself.
        IMPORTANT: DO NOT truncate any existing code with /* ... (Existing styles from Title Slide) ... */, you MUST output the full code.
        If your slides are visually appealing but also functional, you will be rewarded with a bonus.

        The information that should be included on this slide is as follows:
        {slide_content}
        """
        )

        if custom_prompt:
            agenda_slide_prompt = custom_prompt

        logger.info("Generating Agenda slide...")
        starttime = time.time()
        llm_output = generator_llm.call(query=agenda_slide_prompt)['text']
        if time.time() - starttime > 120:
            logger.info(f"LLM output:\n{llm_output}")

        html_code = \
            find_text_in_between_tags(llm_output, 
                                      start_tag="<!DOCTYPE html>", 
                                      end_tag="</html>", 
                                      inclusive=True)

        if review:
            logger.info("Reviewing generated HTML...")
            html_img = self.rndr.renderHTML(html_str=html_code, resize=True, resize_ratio=self.render_resize_ratio)
            review_response = self.reviewer(html_code, html_img, reviewer_llm)
            html_code = review_response['html_code']

        return html_code


    def generate_general_slide(self, query : str, slide_content : str, existing_slide_content : dict, generator_llm : LLM, reviewer_llm : LLM, review : bool = True, custom_prompt : str = None) -> str:
        existing_slides = "\n".join([f"{slide['name']} html code:\n```html\n{slide['html']}\n```\n" for slide in existing_slide_content])
        slide_prompt = textwrap.dedent(
        f"""
        You are a tech consultant, and you have been given the following request:
        "{query}"

        You are trying to create a set of slides for a proposal.
        So far you have created several slides, the html code for these slides are provided below.
        You are now creating another slide, the content of which is outlined under "The information that should be included on this slide is as follows:" below.
        Like the title slide, generate this slide in HTML.

        {existing_slides}

        When generating the slide, take into consideration the following points:
        - Make sure to follow a design style that matches the provided example HTML code to maintain consistency across the presentation.
        - Do not include any info from the title slide that does not belong on any other slide, such as the presenter name, their title, the date and the company logo.
        - Titles should be aligned to the top left-hand side of the slide
        - The font size, to make sure that text fits on the slide. 
          Titles should be 2.3em, subtitles at around 1.3em and normal text should be around 0.9em.
          If the slide content defined below is only a few key words or short sentences, you can increase the subtitle size up to 1.8, and normal text size up to 1.3.
        - Be creative with the slide design. Try your best to use visual elements to both enhance the message and make the slides visually engaging.
        - If relevant, use icons.
            
        This slide will become a template master slide which will define the style of the following slides, so design this slide with great care.
        Do not output any other text other than the html itself.
        IMPORTANT: DO NOT truncate any existing code with /* ... (Existing styles from Title Slide) ... */, you MUST output the full code.
        If your slides are visually appealing but also functional, you will be rewarded with a bonus.

        The information that should be included on this slide is as follows:
        {slide_content}
        """
        )

        logger.info("Generating slide...")
        starttime = time.time()
        llm_output = generator_llm.call(query=slide_prompt)['text']
        if time.time() - starttime > 120:
            logger.info(f"LLM output:\n{llm_output}")

        html_code = \
            find_text_in_between_tags(llm_output, 
                                      start_tag="<!DOCTYPE html>", 
                                      end_tag="</html>", 
                                      inclusive=True)

        if review:
            logger.info("Reviewing generated HTML...")
            html_img = self.rndr.renderHTML(html_str=html_code, resize=True, resize_ratio=self.render_resize_ratio)
            review_response = self.reviewer(html_code, html_img, reviewer_llm)
            html_code = review_response['html_code']

        return html_code