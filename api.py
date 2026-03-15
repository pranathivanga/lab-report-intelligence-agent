from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from parser.pdf_parser import parse_report
from engine.benchmark_loader import load_benchmarks
from engine.risk_engine import analyze_tests
from engine.pattern_engine import detect_patterns
from engine.explanation_engine import generate_explanation
from engine.summary_engine import generate_summary
from engine.question_engine import generate_questions

app = FastAPI()

# CORS (DEV MODE)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        # 1. Parse report
        lab_values = await parse_report(file)

        # 2. Analyze tests + calculate risk score
        test_results, risk_score = analyze_tests(lab_values)

        # 3. Detect patterns
        benchmarks = load_benchmarks()
        patterns = detect_patterns(test_results, benchmarks)

        # 4. Derive risk level
        if risk_score <= 35:
            risk_level = "Low"
        elif risk_score <= 65:
            risk_level = "Moderate"
        else:
            risk_level = "High"

        # 5. Generate explanation
        explanation = generate_explanation(
            test_results,
            risk_score,
            risk_level,
            patterns
        )

        # 6. Summary
        summary = generate_summary(test_results)

        # 7. Questions to ask doctor
        questions = generate_questions(test_results, patterns)

        return {
            "risk_score": risk_score,
            "summary": summary,
            "labValues": test_results,
            "explanation": explanation,
            "questions": questions,
        }

    except Exception as e:
        # Always return safe JSON (never crash frontend)
        print("ANALYZE ERROR:", str(e))

        return {
            "risk_score": 0,
            "summary": {
                "tests_analyzed": 0,
                "normal_count": 0,
                "low_count": 0,
                "high_count": 0,
            },
            "labValues": [],
            "explanation": "We could not analyze this report. Please try a different file.",
            "questions": [],
            "error": str(e),
        }