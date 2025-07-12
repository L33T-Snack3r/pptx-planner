# app.py (Updated with CORS and a bug fix)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# 🔽 --- 1. ADD THIS IMPORT --- 🔽
from fastapi.middleware.cors import CORSMiddleware
from pptx_generation.planner import Planner
from pptx_generation.generation import Generator
from htmlrender.renderer import HTMLRenderer
from llm.llmwrapper import LLM
from dotenv import load_dotenv
import traceback

load_dotenv()
load_dotenv(dotenv_path=r"C:\Users\quand\OneDrive\Desktop\VS Code\pptx-planner\local.env")

class UserInput(BaseModel):
    user_input: str

app = FastAPI(
    title="SlideGen API",
    description="Generate slide outlines and rendered HTML from a user query",
    version="0.1",
    debug=True
)

# 🔽 --- 2. ADD THIS ENTIRE MIDDLEWARE BLOCK --- 🔽
# This allows your frontend (e.g., at http://127.0.0.1:5500) to communicate with your backend API.
origins = ["*"]  # This is a wildcard, good for local development.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, GET, etc.
    allow_headers=["*"],
)
# 🔼 --- END OF MIDDLEWARE BLOCK --- 🔼

# Initialize your LLMs, planner, generator, renderer once
llm_outline = LLM(provider="gemini", model="gemini-1.5-flash") # Note: Adjusted model name from your example. Change if needed.
llm_generate = LLM(provider="gemini", model="gemini-1.5-flash") # Note: Adjusted model name from your example. Change if needed.
planner = Planner()

@app.post("/generate-outline")
async def generate_outline_endpoint(req: UserInput):
    try:
        print(f"✅ API call received for outline generation. Input: '{req.user_input}'") # Added for logging
        
        # 🐞 --- BUG FIX --- 🐞
        # You need to pass the actual user input string, not the Pydantic class type.
        # OLD: query=UserInput
        # NEW: query=req.user_input
        pptx_plan = planner.outline(query=req.user_input, llm=llm_outline)
        
        # The planner.outline function likely returns a dictionary.
        # Make sure the key "response" exists and contains the string you want to return.
        if "response" in pptx_plan and isinstance(pptx_plan["response"], str):
            return pptx_plan["response"]
        else:
            # If the response format is not what you expect, raise an error.
            print(f"❌ Unexpected response format from planner: {pptx_plan}")
            raise HTTPException(status_code=500, detail="Internal server error: Invalid format from planner.")
            
    except Exception as e:
        # It's good practice to log the full traceback for debugging
        print(f"❌ An error occurred: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))