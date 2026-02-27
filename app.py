import streamlit as st
from parser.pdf_parser import (
    extract_text_from_pdf,
    extract_text_from_txt,
    extract_lab_values
)
from engine.benchmark_loader import load_benchmarks
from engine.risk_engine import calculate_risk_score
from engine.pattern_engine import detect_patterns
from engine.explanation_engine import generate_explanation

st.set_page_config(page_title="Lab Report Intelligence Agent")

st.title("🧪 Lab Report Intelligence Agent")
st.caption("⚠ This tool does NOT provide medical diagnosis. It helps understand lab reports.")

uploaded_file = st.file_uploader(
    "Upload Lab Report (PDF or TXT)",
    type=["pdf", "txt"]
)

if uploaded_file:
    # Extract text
    if uploaded_file.name.endswith(".pdf"):
        raw_text = extract_text_from_pdf(uploaded_file)
    else:
        raw_text = extract_text_from_txt(uploaded_file)

    # Structured extraction
    lab_values = extract_lab_values(raw_text)

    st.subheader("Extracted Lab Values")
    st.json(lab_values)

    # Load benchmarks
    benchmarks = load_benchmarks()

    # Risk scoring
    total_score, risk_level, detailed_scores = calculate_risk_score(
        lab_values, benchmarks
    )

    st.subheader("Overall Health Risk")
    st.write(f"Risk Score: **{total_score} / 100**")
    st.write(f"Risk Level: **{risk_level}**")

    st.subheader("Risk Breakdown")
    st.json(detailed_scores)

    # Pattern detection
    patterns = detect_patterns(lab_values, benchmarks)

    st.subheader("Detected Patterns (Non-Diagnostic)")
    if patterns:
        for p in patterns:
            st.write(f"🧠 **{p['pattern']}**")
            st.write(f"Tests involved: {', '.join(p['tests_involved'])}")
            st.write(f"Confidence: {p['confidence_percent']}%")
    else:
        st.write("No significant patterns detected.")

    # AI Explanation
    st.subheader("AI Explanation (Patient-Friendly)")
    explanation = generate_explanation(
        lab_values, total_score, risk_level, patterns
    )
    st.write(explanation)

    st.subheader("Raw Report Text")
    st.text(raw_text)