# Layoff Risk Analyzer

This project analyzes employee data to predict potential layoff risk.
# RiskGuard AI – Smart Career Layoff Risk Predictor

## 📌 Project Overview

**RiskGuard AI** is an AI-powered career intelligence platform that analyzes a professional’s role, skills, and experience to estimate their **layoff risk level**.

The system helps users understand how stable their current career path is and provides **data-driven recommendations for safer career transitions and skill improvements**.

By combining **machine learning, resume parsing, and skill gap analysis**, RiskGuard AI enables professionals to make informed career decisions in a rapidly evolving job market.

---

## 🎯 Key Features

### 1️⃣ Layoff Risk Prediction

* Uses a **Machine Learning model (Random Forest)** to estimate the probability of job layoff risk.
* Considers:

  * Role
  * Skills
  * Years of experience

### 2️⃣ Resume Analyzer

* Upload a **PDF resume**
* Extracts:

  * Role
  * Skills
  * Experience
* Automatically fills the prediction form.

### 3️⃣ Risk Visualization Dashboard

* Displays risk percentage with an **interactive gauge meter**
* Provides **explanations for the risk score**

### 4️⃣ Skill Gap Analysis

* Compares user skills with **industry-required skills**
* Identifies:

  * Skills you already have
  * Skills you need to learn

### 5️⃣ Career Shift Recommendations

* Suggests **safer career paths** with lower layoff risk.
* Shows **match percentage** between current skills and target roles.

### 6️⃣ Learning Resource Recommendations

* Provides curated **courses and learning materials** for missing skills.

### 7️⃣ AI Career Chatbot

* Interactive assistant that gives career advice based on:

  * Risk level
  * Role
  * Skills

---

## 🏗 System Architecture

```
Frontend (React + Vite)
        │
        ▼
FastAPI Backend
        │
        ▼
Machine Learning Model (Random Forest)
        │
        ▼
Resume Parser (PyMuPDF)
        │
        ▼
Career Recommendation Engine
```

---

## ⚙️ Tech Stack

### Frontend

* React.js
* Framer Motion
* Recharts
* Lucide Icons
* Axios

### Backend

* FastAPI
* Python
* Pandas
* NumPy
* Scikit-Learn

### Machine Learning

* Random Forest Regressor
* Feature Encoding
* Skill-Role Matching Logic

### Resume Parsing

* PyMuPDF

---

## 📊 Example Output

```
Role: Machine Learning Engineer
Layoff Risk: 65%
Risk Level: Moderate

Explanation:
• Industry competition is moderate for this role
• Entry-level positions are more sensitive to market changes
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/career-risk.git
cd career-risk
```

---

### 2️⃣ Setup Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install scikit-learn pymupdf python-multipart
```

Run backend:

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 3️⃣ Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 📂 Project Structure

```
career-risk
│
├── backend
│   ├── main.py
│   ├── model
│   ├── routes
│   ├── utils
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   └── data.js
│   └── package.json
│
└── README.md
```

---

## 💡 Future Improvements

* Real-time **job market demand analysis**
* Integration with **LinkedIn job data**
* AI-powered **resume skill extraction using NLP**
* **Career growth simulation engine**

---

## 👨‍💻 Authors

Developed as part of a **career risk prediction and AI career advisory platform** to help professionals navigate uncertain job markets.
