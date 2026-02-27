import streamlit as st
import pandas as pd

from parser.pdf_parser import (
    extract_text_from_pdf,
    extract_text_from_txt,
    extract_lab_values
)
from engine.benchmark_loader import load_benchmarks
from engine.risk_engine import calculate_risk_score
from engine.pattern_engine import detect_patterns
from engine.explanation_engine import generate_explanation


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Lab Report Intelligence Agent",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("🧪 Lab Report Intelligence Agent")

st.write(
    "This tool helps you understand your medical lab report in simple language. "
    "It highlights values that may need attention. "
    "This is not a medical diagnosis."
)

st.markdown("---")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload your lab report (PDF or TXT)",
    type=["pdf", "txt"]
)

if uploaded_file:

    # -------- TEXT EXTRACTION --------
    if uploaded_file.name.endswith(".pdf"):
        raw_text = extract_text_from_pdf(uploaded_file)
    else:
        raw_text = extract_text_from_txt(uploaded_file)

    # -------- LAB VALUE EXTRACTION --------
    lab_values = extract_lab_values(raw_text)

    # -------- LOAD BENCHMARKS --------
    benchmarks = load_benchmarks()

    # -------- RISK SCORING --------
    total_score, risk_level, _ = calculate_risk_score(
        lab_values, benchmarks
    )

    # -------- PATTERN DETECTION --------
    patterns = detect_patterns(lab_values, benchmarks)

    # -------- AI EXPLANATION --------
    explanation = generate_explanation(
        lab_values, total_score, risk_level, patterns
    )

    # ---------------- RISK SUMMARY ----------------
    st.subheader("📊 Overall Health Risk")
    st.progress(int(total_score))
    st.write(f"Risk Score: **{total_score} / 100**")
    st.write(f"Risk Level: **{risk_level}**")

    st.markdown("---")

    # ---------------- LAB RESULTS TABLE ----------------
    st.subheader("📋 Your Lab Results")

    rows = []
    for test, value in lab_values.items():
        mn, mx = benchmarks[test]["range"]

        if value < mn:
            status = "Low"
        elif value > mx:
            status = "High"
        else:
            status = "Normal"

        rows.append({
            "Test": test,
            "Your Value": value,
            "Normal Range": f"{mn} – {mx}",
            "Status": status
        })

    df = pd.DataFrame(rows)
    st.table(df)

    st.markdown("---")

    # ---------------- EXPLANATION ----------------
    st.subheader("🧠 What This Means")
    st.write(explanation)

    st.markdown("---")
    st.caption(
        "ℹ This tool is for educational purposes only. "
        "Please consult a qualified doctor for medical advice."
    )