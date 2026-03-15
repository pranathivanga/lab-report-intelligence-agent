🧠 Lab Report Intelligence Agent

An AI-powered system that converts complex medical lab reports into structured, easy-to-understand health insights.

Instead of overwhelming users with raw numbers and medical terminology, the system analyzes lab values and generates plain-language explanations and summaries, while maintaining a strictly non-diagnostic approach.

🚨 Problem

Medical lab reports contain complex terminology, abbreviations, and numerical ranges that are difficult for non-medical users to interpret.

This often leads to:

confusion about health status

unnecessary anxiety

misinterpretation of results

Most patients simply want to understand:

“Is this normal? Should I be concerned?”

💡 Solution

Lab Report Intelligence Agent processes uploaded lab reports and converts them into structured, human-readable insights.

The system:

extracts lab values from reports

compares them against standard reference ranges

highlights abnormal results

generates AI-powered explanations in plain English

The goal is to improve health literacy, not provide medical diagnoses.

✨ Key Features

📄 Upload lab reports (PDF / TXT)

🔍 Automatic lab value extraction

📊 Overall risk score visualization

⚡ “At a Glance” summary of results

🤖 AI-generated explanations in simple language

📈 Interpretation confidence indicators

💬 Suggested questions to ask your doctor

🏗 System Architecture
```
User
  ↓
Next.js Frontend (Vercel)
  ↓
FastAPI Backend (Render)
  ↓
Gemini AI API
  ↓
Structured Health Insights
```
🛠 Tech Stack
Frontend

Next.js

React

Tailwind CSS

Backend

FastAPI

Python

Data Processing

PDFPlumber

Regex-based parsing

AI Integration

Google Gemini API

Deployment

Vercel (Frontend)

Render (Backend)

🌐 Live Demo

Frontend
https://lab-report-intelligence-agent-e11q.vercel.app

Backend API
https://lab-report-intelligence-agent-1.onrender.com/docs

▶️ Running Locally
1️⃣ Start Backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn api:app --reload

Backend runs at:

http://127.0.0.1:8000
2️⃣ Start Frontend
cd frontend
npm install
npm run dev

Open in browser:

http://localhost:3000
⚠ Disclaimer

This application is intended for informational purposes only and does not constitute medical advice, diagnosis, or treatment.

Always consult a qualified healthcare professional regarding medical concerns.

📌 Future Improvements

Support for additional lab report formats

Improved medical entity recognition

Multi-report comparison

Personalized health trend tracking
