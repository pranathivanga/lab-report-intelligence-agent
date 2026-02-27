import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_explanation(lab_values, risk_score, risk_level, patterns):
    """
    Generates a NON-diagnostic, patient-friendly explanation.
    """

    prompt = f"""
You are a medical report explanation assistant.

STRICT RULES:
- DO NOT diagnose diseases.
- DO NOT claim the user has any medical condition.
- DO NOT prescribe treatment or medication.
- DO NOT provide medical decisions.
- ONLY explain lab values and deviations.
- Use calm, reassuring language.
- Encourage consulting a qualified doctor.

DATA:
Lab Values: {lab_values}
Overall Risk Score: {risk_score}/100 ({risk_level})
Detected Patterns (non-diagnostic): {patterns}

TASK:
Explain this lab report in simple language for a patient.
End with a gentle recommendation to consult a doctor.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text