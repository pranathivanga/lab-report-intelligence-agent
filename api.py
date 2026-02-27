from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

from parser.pdf_parser import extract_text_from_pdf, extract_lab_values
from engine.benchmark_loader import load_benchmarks
from engine.risk_engine import calculate_risk_score
from engine.pattern_engine import detect_patterns
from engine.explanation_engine import generate_explanation

app = FastAPI()

# ✅ Allow frontend (React) to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ✅ Handle PDF vs TXT correctly
    if file.filename.endswith(".pdf"):
        raw_text = extract_text_from_pdf(file_location)

    elif file.filename.endswith(".txt"):
        with open(file_location, "r", encoding="utf-8") as f:
            raw_text = f.read()

    else:
        return {"error": "Unsupported file format"}

    # ✅ These lines MUST be outside if/elif/else
    lab_values = extract_lab_values(raw_text)
    benchmarks = load_benchmarks()

    total_score, risk_level, _ = calculate_risk_score(lab_values, benchmarks)
    patterns = detect_patterns(lab_values, benchmarks)
    explanation = generate_explanation(
        lab_values, total_score, risk_level, patterns
    )

    return {
        "risk_score": total_score,
        "risk_level": risk_level,
        "lab_values": lab_values,
        "patterns": patterns,
        "explanation": explanation
    }