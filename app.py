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
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #f8fafc, #eef2ff);
}

.main-title {
    font-size: 40px;
    font-weight: 700;
    color: #1e293b;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

.low { color: #16a34a; font-weight: 600; }
.moderate { color: #f59e0b; font-weight: 600; }
.high { color: #dc2626; font-weight: 600; }

.footer {
    font-size: 12px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown('<div class="main-title">🧪 Lab Report Explained</div>', unsafe_allow_html=True)

st.markdown("""
Understand your lab report clearly and confidently.

This tool explains your results in simple language and highlights values that may need attention.

⚠ This tool does NOT provide medical diagnosis or treatment.
""")

st.markdown("---")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload your lab report (text-based PDF or TXT file)",
    type=["pdf", "txt"]
)

if uploaded_file:

    # TEXT EXTRACTION
    if uploaded_file.name.endswith(".pdf"):
        raw_text = extract_text_from_pdf(uploaded_file)
    else:
        raw_text = extract_text_from_txt(uploaded_file)

    lab_values = extract_lab_values(raw_text)
    benchmarks = load_benchmarks()

    total_score, risk_level, detailed_scores = calculate_risk_score(
        lab_values, benchmarks
    )

    patterns = detect_patterns(lab_values, benchmarks)

    explanation = generate_explanation(
        lab_values, total_score, risk_level, patterns
    )

    # ---------------- RISK CARD ----------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Overall Health Risk")

    if risk_level == "Low":
        css_class = "low"
    elif risk_level == "Moderate":
        css_class = "moderate"
    else:
        css_class = "high"

    st.markdown(f'<span class="{css_class}">Risk Level: {risk_level}</span>', unsafe_allow_html=True)
    st.progress(int(total_score))
    st.write(f"Risk Score: {total_score} / 100")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- LAB RESULTS CARD ----------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Your Lab Results")

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
    st.dataframe(df, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- EXPLANATION CARD ----------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("What This Means")

    st.write(explanation)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- FOOTER ----------------
    st.markdown('<div class="footer">For educational purposes only. Please consult a qualified doctor for medical advice.</div>', unsafe_allow_html=True)