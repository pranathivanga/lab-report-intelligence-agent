##🧠 LAB REPORT INTELLIGENCE AGENT


🚨 PROBLEM STATEMENT

Lab reports contain complex medical terminology and numerical values that are difficult for non-medical users to understand. This often causes confusion, anxiety, and misinterpretation of personal health data.

💡 OUR SOLUTION

Lab Report Intelligence Agent converts raw lab reports into structured, plain-language insights that help users understand their health data clearly — without providing medical diagnosis.

✨ UNIQUE INNOVATION

We don’t just display lab values.
We structure understanding by:

Providing a high-level summary first

Categorizing results as normal, low, or high

Explaining values in simple language

Maintaining a strictly non-diagnostic, patient-safe design

Our focus is health literacy, not diagnosis.

🔑 KEY FEATURES

Upload lab reports (PDF / TXT)

Automatic lab value extraction

Overall health risk summary

“At a Glance” report overview

Plain-language explanation

🛠 TECH STACK

Frontend: Next.js, React, Tailwind CSS
Backend: FastAPI (Python)
Parsing: PDFPlumber, Regex
AI Integration: Gemini API

▶️ How to Run Locally


Backend


cd backend
venv\Scripts\activate
uvicorn api:app --port 8001


Frontend


cd frontend
npm install
npm run dev

Open in browser:
http://localhost:3000

⚠ DISCLAIMER

This application is for informational purposes only and does not replace professional medical advice.
