import os
import io
import logging
import pickle
import PyPDF2
import google.generativeai as genai
import numpy as np

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi.middleware.cors import CORSMiddleware

# -------------------------------------------------
# FastAPI app
app = FastAPI(title="Resume Scorer + Suggestion API")
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -------------------------------------------------
# Logging setup
logging.basicConfig(level=logging.INFO)

# -------------------------------------------------
# FastAPI app
app = FastAPI(title="Resume Scorer + Suggestion API")

# -------------------------------------------------
try:
    with open("vectorizer.pkl", "rb") as f:
        vectorizer: TfidfVectorizer = pickle.load(f)

    with open("resume_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    vectorizer = TfidfVectorizer()
    logging.warning("Vectorizer and model pickle files not found. Scoring will not be functional.")
except Exception as e:
    logging.error(f"Error loading ML models: {e}")
    vectorizer = TfidfVectorizer()

# -------------------------------------------------
# Gemini API configuration
genai.configure(api_key="AIzaSyA7wVFNP42PMGrDieQL-CHl4PdDSIHbgoE")


# -------------------------------------------------
# Helper: Extract text from PDF
def extract_text_from_pdf(file: UploadFile) -> str:
    try:
        pdf_reader = PyPDF2.PdfReader(file.file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        logging.error(f"Error extracting text: {e}")
        raise HTTPException(status_code=400, detail="Invalid PDF file.")

# -------------------------------------------------
# Helper: Get LLM Suggestions
def get_resume_suggestions(resume_text: str, job_description: str):
    prompt = f"""
    You are an expert resume analyst. Provide a short and clear analysis (max 80 words).

    Compare this resume to the job description:
    - Identify missing skills/keywords
    - Suggest improvements in bullet points
    - Highlight how to better align with the role

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Suggestions:
    """

    try:
        model_llm = genai.GenerativeModel("gemini-2.0-flash")
        response = model_llm.generate_content(prompt)
        return response.text
    except Exception as e:
        logging.error(f"Gemini API failed: {e}")
        return "Could not generate suggestions. Please try again later."

# -------------------------------------------------
# Pydantic models for request bodies
class ScoreRequest(BaseModel):
    resume_text: str
    job_description: str

class SuggestionsRequest(BaseModel):
    resume_text: str
    job_description: str
    
# -------------------------------------------------
# Endpoint: Score
@app.post("/score/")
async def score_resume(job_description: str = Form(...),resume_file: UploadFile = File(...)):
    try:
        resume_text = extract_text_from_pdf(resume_file)
        combined_text = job_description + " " + resume_text
        vector = vectorizer.transform([combined_text])
        score = model.predict(vector)[0]
        score = round(float(score), 2)
        return {"match_score": score}

    except Exception as e:
        logging.error(f"Scoring failed: {e}")
        raise HTTPException(status_code=500, detail="Scoring model failed.")

# -------------------------------------------------
# Endpoint: Suggestions
@app.post("/suggestions/")
async def get_ai_suggestions(job_description: str = Form(...), resume_file: UploadFile = File(...)):
    resume_text = extract_text_from_pdf(resume_file)
    suggestions = get_resume_suggestions(resume_text, job_description)
    return {"suggestions": suggestions}
