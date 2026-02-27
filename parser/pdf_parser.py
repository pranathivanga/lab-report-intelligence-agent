import pdfplumber
import re

# -------- PDF TEXT EXTRACTION --------

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


# -------- TXT FILE EXTRACTION (FOR DEMO SAFE MODE) --------
def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8")


# -------- LAB VALUE EXTRACTION USING REGEX --------
def extract_lab_values(raw_text):
    lab_data = {}

    patterns = {
        "Hemoglobin": r"Hemoglobin\s+([\d\.]+)",
        "RBC": r"RBC\s+([\d\.]+)",
        "MCV": r"MCV\s+([\d\.]+)",
        "Fasting Glucose": r"Fasting Glucose\s+([\d\.]+)",
        "LDL Cholesterol": r"LDL Cholesterol\s+([\d\.]+)"
    }

    for test, pattern in patterns.items():
        match = re.search(pattern, raw_text, re.IGNORECASE)
        if match:
            lab_data[test] = float(match.group(1))

    return lab_data