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
    page_title="Lab Report Explained",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("🧪 Lab Report Explained")

st.markdown(
    """
    **This tool helps you understand your medical lab report in simple language.**  
    It explains what your numbers mean and highlights values that may need attention.

    ⚠ **Important:**  
    This tool does **not** provide medical diagnosis or treatment.  
    Always consult a qualified doctor for medical advice.
    """
)

st.markdown("---")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload your lab report (text-based PDF or TXT file)",
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
    total_score, risk_level, detailed_scores = calculate_risk_score(
        lab_values, benchmarks
    )

    # -------- PATTERN DETECTION --------
    patterns = detect_patterns(lab_values, benchmarks)

    # -------- AI EXPLANATION --------
    explanation = generate_explanation(
        lab_values, total_score, risk_level, patterns
    )

    # ================= UI BLOCK 2 (Risk Summary) =================
    st.subheader("📊 Overall Health Risk")

    if risk_level == "Low":
        risk_color = "🟢"
        msg = "Your overall risk appears to be low."
    elif risk_level == "Moderate":
        risk_color = "🟡"
        msg = "Some values need attention."
    else:
        risk_color = "🔴"
        msg = "Several values are outside the normal range."

    st.markdown(f"### {risk_color} Risk Level: **{risk_level}**")
    st.progress(int(total_score))
    st.write(f"**Risk Score:** {total_score} / 100")
    st.write(msg)

    st.markdown("---")

    # ================= UI BLOCK 3 (Lab Results Table) =================
    st.subheader("📋 Your Lab Results")

    table_rows = []

    for test, value in lab_values.items():
        normal_min, normal_max = benchmarks[test]["range"]

        if value < normal_min:
            status = "Low"
        elif value > normal_max:
            status = "High"
        else:
            status = "Normal"

        table_rows.append({
            "Test": test,
            "Your Value": value,
            "Normal Range": f"{normal_min} – {normal_max}",
            "Status": status
        })

    df = pd.DataFrame(table_rows)
    st.table(df)

    st.markdown("---")

    # ================= EXPLANATION =================
    st.subheader("🧠 What This Means")
    st.write(explanation)

    st.markdown("---")
    st.caption(
        "ℹ This information is for educational purposes only and is not a medical diagnosis."
    )