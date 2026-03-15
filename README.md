🧠 Lab Report Intelligence Agent

AI-powered system that converts complex medical lab reports into clear, structured health insights.
The platform analyzes lab values and generates plain-language explanations to help users understand their health data.

🚨 Problem

Medical lab reports contain complex terminology and numerical ranges that are difficult for non-medical users to interpret.

This often leads to:

confusion about results

unnecessary anxiety

misinterpretation of health data

Most patients simply want to know:

“Is this normal?”

💡 Solution

Lab Report Intelligence Agent processes uploaded reports and converts them into easy-to-understand insights.

The system:

extracts lab values from reports

identifies normal / abnormal results

summarizes findings clearly

generates AI explanations in simple language

The goal is health literacy, not diagnosis.

✨ Key Features

📄 Upload lab reports (PDF / TXT)

🔍 Automatic lab value extraction

📊 Overall risk score summary

⚡ “At a Glance” results overview

🤖 AI-generated explanations

💬 Suggested questions to ask a doctor

🏗 System Architecture
```
User
 │
 ▼
Next.js Frontend (Vercel)
 │
 ▼
FastAPI Backend (Render)
 │
 ▼
Gemini AI
 │
 ▼
Structured Health Insights
```
🛠 Tech Stack
Frontend

Next.js • React • Tailwind CSS

Backend

FastAPI • Python

Data Processing

PDFPlumber • Regex parsing

AI

Google Gemini API

Deployment

Vercel (Frontend)
Render (Backend)

🌐 Live Demo

Frontend
https://lab-report-intelligence-agent-e11q.vercel.app

Backend API
https://lab-report-intelligence-agent-1.onrender.com/docs
