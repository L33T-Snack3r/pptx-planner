import sys
from loguru import logger
from llm.llmwrapper import LLM
from utils.utils import find_text_in_between_tags
import textwrap

class Planner():
    
    def brainstorm(self, query : str, llm : LLM) -> str:
        
        brainstorm_prompt = textwrap.dedent(
        f"""
        You are a tech consultant, and you have been given the following request:

        "{query}"

        Before starting work on the request, you need to brainstorm.
        From a technical perspective, how could something like this be done? 
        Please use the following pointers to guide your thought process:
        - What is the most cutting-edge way to do this?
        - How can this be done using cloud services?
        """
        )

        logger.info(
            textwrap.dedent(
                f"""PPTX Planning STEP 1: Brainstorming implementation approach based on user query...
                    QUERY: "{query}"
                """
            )
        )

        brainstorm_response = llm.call(query=brainstorm_prompt)['text']

        logger.info("PPTX Planning STEP 1: Brainstorming complete!")

        return {'prompt' : brainstorm_prompt, 'response' : brainstorm_response}


    def outline(self, query : str, brainstorm_response : str, llm : LLM) -> str:
        outline_prompt = textwrap.dedent(
            f"""
            You are a tech consultant, and you have been given the following request:

            "{query}"

            After consulting with a senior software engineer, he has provided you the following approach to build such a system:
            "{brainstorm_response}"

            It is now time for you to create the proposal slides.
            Before deciding on what content should go on the slides, 
            create a well-thought out plan of the structure that this presentation should follow.

            Some of the sections you should include are:
            - Title slide
            - Executive summary slide
            - The background of the problem
            - Your proposed solution and why it will work / benefits of the solution
            - The infrastructure and tech stack
            - The required human resources
            - The timeline
            - The cost involved in this project
            - A proper conclusion slide

            Depending on the situation, be creative and add in any other sections that you think might add value.
            If this proposal is successful, you will get a big raise!
            """
        )
    
        logger.info("PPTX Planning STEP 2: Creating high-level Presentation outline...")

        outline_response = llm.call(query=outline_prompt)['text']

        logger.info("PPTX Planning STEP 2: Outline creation complete!")

        return {'prompt' : outline_prompt, 'response' : outline_response}


    def slide_content(self, query : str, brainstorm_response : str, outline_response : str, llm : LLM) -> str:
        slide_content_prompt = textwrap.dedent(
            f"""
            You are a tech consultant, and you have been given the following request:

            "{query}"

            After consulting with a senior software engineer, he has provided you the following approach to build such a system:
            "{brainstorm_response}"

            Based on the advice of the senior software engineer, you have planned out your presentation:
            "{outline_response}"

            Following the plan you have created above, and referencing the technical advice of the senior software engineer,
            describe the content that will appear on EACH slide in detail.

            Pay extra attention to the following points:
            1) If a diagram or image should go on a slide (e.g. an infrastructure diagram, organization chart or a GANTT chart etc.), 
            you must describe it with enough detail such that someone reading the description would be able to reproduce it perfectly.

            2) This slide content plan will be passed on to another person, so the slide descriptions must be as precise and specific as possible.

            3) Think carefully about whether or not the needs of the client are being met with this proposal.

            4) Make sure to include the content that should appear on the title slide.

            If this proposal is successful, you will get a big raise!

            IMPORTANT: Make sure to separate the content of each slide with the following markers <Slide X START> and <Slide X END>, where X represents the slide number.
            """
        )

        logger.info("PPTX Planning STEP 3: Defining the content to appear on each slide...")

        slide_content_response =  llm.call(query=slide_content_prompt)['text']

        logger.info("PPTX Planning STEP 3: Slide content creation complete!")

        return {'prompt' : slide_content_prompt, 'response' : slide_content_response} 


    def extract_flags(self, text: str, startflag : str = '<', endflag : str = '>' ) -> list:
        """
        Get all <Slide 1 START> <Slide 1 END> Flags
        """
        flags = []
        start = 0
        while True:
            start = text.find(startflag, start)
            if start == -1:
                break
            end = text.find(endflag, start)
            if end == -1:
                break

            flags.append(text[start:end+1])
            start = end + 1
        
        if len(flags) % 2 != 0:
            raise Exception(f"Uneven number of separation flags. Start and End flags come in pairs")

        return flags

    def extract_slide_content(self, slide_content_response : str) -> dict:

        flags = self.extract_flags(slide_content_response)

        template_master, content = [], {}
        slidenum = 1

        for i in range(0,len(flags),2):

            slide_content = find_text_in_between_tags(slide_content_response, flags[i], flags[i + 1])
            content[f"slide_{slidenum}"] = slide_content

            if slidenum in (1,2) or 'conclusion' in slide_content.lower():
                template_master.append(f"slide_{slidenum}")
            slidenum += 1

        return {'slide_content' : content, 'template_slides' : template_master}


    def plan_content(self,  query : str, llm_1 : LLM, llm_2 : LLM = None, llm_3 : LLM = None) -> dict:
        """
        Main planning function
        """

        brainstorm_llm = llm_1
        outline_llm = llm_2 if llm_2 is not None else llm_1
        slide_content_llm = llm_3 if llm_3 is not None else llm_1

        # 1. Brainstorm
        brainstorm_output = self.brainstorm(query=query, llm=brainstorm_llm) 

        # 2. Create high-level slide outline
        outline_output = self.outline(query=query, brainstorm_response=brainstorm_output['response'], llm=outline_llm)

        # 3. Create detailed slide content at a slide granularity
        slide_content_output = self.slide_content(query=query, 
                                                    brainstorm_response=brainstorm_output['response'], 
                                                    outline_response=outline_output['response'],
                                                    llm=slide_content_llm
                                                    )
        
        # 4. Extract slide content
        processed_slide_content_output = self.extract_slide_content(slide_content_response=slide_content_output['response'])

        return {'brainstorm' : brainstorm_output, 
                'outline' : outline_output, 
                'unprocessed_slide_content' : slide_content_output, 
                'processed_slide_content' : processed_slide_content_output
                }




