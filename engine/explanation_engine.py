import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_explanation(lab_values, risk_score, risk_level, patterns):
    """
    Generates a NON-diagnostic, patient-friendly explanation.
    """

    prompt = f"""
You are a medical report explanation assistant.

IMPORTANT RULES:
- DO NOT diagnose diseases.
- DO NOT name medical conditions as final conclusions.
- DO NOT prescribe treatment or medication.
- ONLY explain lab values, deviations, and general implications.
- Encourage consulting a medical professional when needed.
- Use calm, reassuring language.

INPUT DATA:
Lab Values: {lab_values}
Overall Risk Score: {risk_score}/100 ({risk_level})
Detected Patterns: {patterns}

TASK:
Explain the lab report in simple language for a patient.
Focus on understanding, not diagnosis.
End with a general recommendation about consulting a doctor.
"""

    response = model.generate_content(prompt)
    return response.text