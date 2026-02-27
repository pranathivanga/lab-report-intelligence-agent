import streamlit as st
from parser.pdf_parser import (
    extract_text_from_pdf,
    extract_text_from_txt,
    extract_lab_values
)
from engine.benchmark_loader import load_benchmarks
from engine.risk_engine import calculate_risk_score

st.set_page_config(page_title="Lab Report Intelligence Agent")

st.title("🧪 Lab Report Intelligence Agent")

uploaded_file = st.file_uploader(
    "Upload Lab Report (PDF or TXT)",
    type=["pdf", "txt"]
)

if uploaded_file:
    # Extract raw text
    if uploaded_file.name.endswith(".pdf"):
        raw_text = extract_text_from_pdf(uploaded_file)
    else:
        raw_text = extract_text_from_txt(uploaded_file)

    # Extract structured lab values
    lab_values = extract_lab_values(raw_text)

    st.subheader("Extracted Lab Values")
    st.json(lab_values)

    # Load medical benchmarks
    benchmarks = load_benchmarks()

    st.subheader("Loaded Medical Benchmarks")
    st.json(benchmarks)

    # Calculate risk
    total_score, risk_level, detailed_scores = calculate_risk_score(
        lab_values, benchmarks
    )

    st.subheader("Overall Health Risk")
    st.write(f"Risk Score: **{total_score} / 100**")
    st.write(f"Risk Level: **{risk_level}**")

    st.subheader("Risk Breakdown")
    st.json(detailed_scores)

    st.subheader("Raw Report Text")
    st.text(raw_text)