# 🧠 Lab Report Intelligence Agent

AI-powered system that converts complex medical lab reports into **clear, structured health insights**.

Instead of overwhelming users with raw numbers and medical terminology, the system analyzes lab values and generates **plain-language explanations** while maintaining a strictly **non-diagnostic approach**.

---

## 🚨 Problem

Medical lab reports contain complex terminology and numerical ranges that are difficult for non-medical users to interpret.

This often leads to:

- confusion about health results  
- unnecessary anxiety  
- misinterpretation of lab values  

Most patients simply want to understand:

> **“Is this normal?”**

---

## 💡 Solution

Lab Report Intelligence Agent processes uploaded lab reports and converts them into **human-readable insights**.

The system:

- extracts lab values from reports  
- identifies normal / abnormal results  
- summarizes health indicators  
- generates AI explanations in simple language  

The goal is to improve **health literacy**, not provide medical diagnosis.

---

## ✨ Key Features

- 📄 Upload lab reports *(PDF / TXT)*
- 🔎 Automatic lab value extraction
- 📊 Overall risk score visualization
- ⚡ “At a Glance” report summary
- 🤖 AI-generated explanations
- 📈 Interpretation confidence indicators
- 💬 Suggested questions to ask a doctor

---

## 🏗 System Architecture
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
## 🛠 Tech Stack

### Frontend
Next.js  
React  
Tailwind CSS  

### Backend
FastAPI  
Python  

### Data Processing
PDFPlumber  
Regex parsing  

### AI Integration
Google Gemini API  

### Deployment
Vercel (Frontend)  
Render (Backend)

---

## 🌐 Live Demo

Frontend  
https://lab-report-intelligence-agent-e11q.vercel.app

Backend API  
https://lab-report-intelligence-agent-1.onrender.com/docs

---

## ▶️ Run Locally

### Start Backend

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn api:app --reload

Backend runs at:

http://127.0.0.1:8000
Start Frontend
cd frontend
npm install
npm run dev

Open in browser:

http://localhost:3000
