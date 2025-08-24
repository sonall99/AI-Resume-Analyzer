import os
import logging
import joblib
import PyPDF2
import google.generativeai as genai
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi.middleware.cors import CORSMiddleware

# -------------------------------------------------
# Logging setup
logging.basicConfig(level=logging.INFO)

# -------------------------------------------------
# FastAPI app 
app = FastAPI(title="Resume Scorer + Suggestion API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# Load ML model + vectorizer (joblib only)
try:
    vectorizer: TfidfVectorizer = joblib.load("final_vectorizer.joblib")
    model = joblib.load("final_model.joblib")
    logging.info("✅ Vectorizer and model loaded successfully.")
except FileNotFoundError:
    vectorizer = None
    model = None
    logging.warning("⚠️ Vectorizer/model files not found. Scoring will not work.")
except Exception as e:
    vectorizer = None
    model = None
    logging.error(f"❌ Error loading ML models: {e}")

# -------------------------------------------------
# Gemini API config
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AIzaSyA7wVFNP42PMGrDieQL-CHl4PdDSIHbgoE"))

# -------------------------------------------------
# Helper: Extract text from PDF
def extract_text_from_pdf(file: UploadFile) -> str:
    try:
        pdf_reader = PyPDF2.PdfReader(file.file)
        text = "".join([page.extract_text() or "" for page in pdf_reader.pages])
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
    """
    try:
        model_llm = genai.GenerativeModel("gemini-2.0-flash")
        response = model_llm.generate_content(prompt)
        return response.text
    except Exception as e:
        logging.error(f"Gemini API failed: {e}")
        return "❌ Could not generate suggestions. Please try again later."

# -------------------------------------------------
# Endpoints

@app.post("/score/")
async def score_resume(job_description: str = Form(...), resume_file: UploadFile = File(...)):
    if model is None or vectorizer is None:
        raise HTTPException(status_code=500, detail="Scoring model not available.")
    try:
        resume_text = extract_text_from_pdf(resume_file)
        combined_text = job_description + " " + resume_text
        vector = vectorizer.transform([combined_text])
        score = model.predict(vector)[0]
        return {"match_score": round(float(score), 2)}
    except Exception as e:
        logging.error(f"Scoring failed: {e}")
        raise HTTPException(status_code=500, detail="Scoring model failed.")

@app.post("/suggestions/")
async def get_ai_suggestions(job_description: str = Form(...), resume_file: UploadFile = File(...)):
    resume_text = extract_text_from_pdf(resume_file)
    suggestions = get_resume_suggestions(resume_text, job_description)
    return {"suggestions": suggestions}
