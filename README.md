# 🎓 CareerAgent OS: The Agentic AI Career Mentor

![Project Status](https://img.shields.io/badge/Status-Hackathon_Submission-success?style=for-the-badge&color=2ea44f)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Llama3](https://img.shields.io/badge/AI-Llama_3_70B-purple?style=for-the-badge)

### **Team Name:** [Insert Your Team Name Here]
**Problem Statement ID:** Agentic AI - Career Development Assistant

---

## 📖 Overview
**CareerAgent OS** is an autonomous **Agentic AI System** designed to solve the "Decision Paralysis" students face in their early careers.

Unlike traditional chatbots that simply answer questions, CareerAgent OS acts as a long-term mentor. It uses a **Closed-Loop Feedback System** to track a student's **Cognitive State** (using **Bloom's Taxonomy**) and dynamically adapts their learning roadmap in real-time based on their actual progress and live 2025 market data.

---

## 🚀 Key Features

### 1. 🧠 Cognitive Diagnosis Engine
Instead of just tracking "done/not done," the Agent analyzes user journals to detect **Learning Gaps**:
* **Recall Gap:** Forgetting syntax or basic facts.
* **Concept Gap:** Misunderstanding underlying logic.
* **Application Gap:** Inability to apply theory to code.

### 2. ⚡ Real-Time Learning Velocity
The system calculates a "Velocity Score" based on past performance to adjust the pacing of future tasks (e.g., slowing down if burnout is detected).

### 3. 🌍 Live Market Alignment
Integrated with **DuckDuckGo Search**, the Agent scans for **2025 Job Market Trends** to ensure the roadmap is never outdated.

### 4. 🔄 Autonomous Feedback Loop
A **Supervisor Agent** orchestrates the entire workflow, managing long-term memory (`memory.json`) and deciding when to trigger a roadmap intervention.

---

## 🛠️ Technology Stack

| Component | Technology Used | Purpose |
| :--- | :--- | :--- |
| **Frontend** | **Streamlit** | Responsive, glassmorphism-styled dashboard. |
| **Intelligence** | **Meta Llama-3 70B** | High-reasoning LLM via **Groq LPU** for <300ms latency. |
| **Orchestration** | **Python (Custom)** | State machine logic for the Supervisor Agent. |
| **Knowledge** | **DuckDuckGo** | Live web search for real-time market data. |
| **Persistence** | **JSON** | Lightweight, portable long-term memory. |

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/CareerAgent-OS.git](https://github.com/YOUR_USERNAME/CareerAgent-OS.git)
cd CareerAgent-OS
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Configure API Key
Important: This project uses the Groq API for high-speed inference.

Get a free API Key from Groq Console.

Open the file llm.py.

Replace the placeholder with your key in the "llm.py" file
```bash
MY_API_KEY = "gsk_..." # Paste your key here
```

### 4. Run the appilication
```bash
streamlit run app.py
```

### 📖 Usage Guide
Phase 1: Strategic Planning
Launch the app.

In the Left Panel, enter your target role (e.g., "Full Stack Developer").

Click "Generate Roadmap".

The Agent scans the web for 2025 skills and creates a personalized 6-month plan.

Phase 2: The Feedback Loop (The "Agentic" Part)
After studying, go to the Right Panel.

Write a reflection in the journal (e.g., "I tried building the API but kept getting 404 errors and forgot how routes work.").

Click "Analyze Progress".

The system will:

Diagnose the specific gap (e.g., Application Gap).

Update your "Mastery Score."

Dynamically rewrite your next steps (e.g., assigning debugging drills instead of new theory).

