import pdfplumber
import re
from fastapi import UploadFile
import tempfile
import os

# --------------------------------------------------
# PDF TEXT EXTRACTION
# --------------------------------------------------
def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


# --------------------------------------------------
# TXT FILE EXTRACTION
# --------------------------------------------------
def extract_text_from_txt(uploaded_file: UploadFile) -> str:
    return uploaded_file.file.read().decode("utf-8", errors="ignore")


# --------------------------------------------------
# LAB VALUE EXTRACTION (FIXED REGEX)
# --------------------------------------------------
def extract_lab_values(raw_text: str) -> dict:
    lab_data = {}

    # 🔴 FLEXIBLE REGEX — THIS IS THE ACTUAL FIX
    patterns = {
    "Hemoglobin": r"Hemoglobin\s+(\d+\.?\d*)",
    "RBC": r"RBC\s+(\d+\.?\d*)",
    "MCV": r"MCV\s+(\d+\.?\d*)",
    "Fasting Glucose": r"Fasting\s+Glucose\s+(\d+\.?\d*)",
    "LDL Cholesterol": r"LDL\s+Cholesterol\s+(\d+\.?\d*)",
}

    for test, pattern in patterns.items():
        match = re.search(pattern, raw_text, re.IGNORECASE | re.DOTALL)
        if match:
            try:
                lab_data[test] = float(match.group(1))
            except ValueError:
                pass  # skip malformed numbers safely

    return lab_data


# --------------------------------------------------
# MAIN ENTRY POINT USED BY API
# --------------------------------------------------
async def parse_report(uploaded_file: UploadFile) -> dict:
    """
    Unified parser used by FastAPI /analyze endpoint.
    Handles PDF and TXT and returns extracted lab values.
    """

    filename = uploaded_file.filename.lower()

    # ---------- PDF ----------
    if filename.endswith(".pdf"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            content = await uploaded_file.read()
            tmp.write(content)
            tmp_path = tmp.name

        try:
            raw_text = extract_text_from_pdf(tmp_path)
        finally:
            os.remove(tmp_path)

    # ---------- TXT ----------
    elif filename.endswith(".txt"):
        content = await uploaded_file.read()
        raw_text = content.decode("utf-8", errors="ignore")

    else:
        raise ValueError("Unsupported file type. Upload PDF or TXT.")

    # DEBUG (optional, remove later)
    print("RAW TEXT:")
    print(raw_text)

    lab_values = extract_lab_values(raw_text)

    print("EXTRACTED VALUES:", lab_values)

    return lab_values