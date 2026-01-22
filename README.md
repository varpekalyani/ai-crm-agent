## 🤖 AI CRM Agent – Healthcare Interaction Automation

###-An AI-powered CRM Agent built to automate, analyze, and optimize healthcare professional (HCP) interactions using intelligent tools and agent-based workflows.
###-This project demonstrates how AI agents can log, summarize, classify, and generate follow-ups for CRM data — reducing manual effort and improving decision-making.

## 🧠 Problem Statement

-In healthcare CRM systems, interactions with doctors are often:
  Manually logged
  Poorly summarized
  Hard to analyze
  Time-consuming to follow up
  This leads to inefficiency and missed insights.

## 💡 Solution

-This project introduces an AI CRM Agent that:
-Accepts raw interaction data
-Uses AI tools to process it intelligently
-Produces structured, actionable outputs
-All through a clean React frontend and a FastAPI backend.

## ⚙️ Tech Stack

-Frontend
-React.js
-CSS (custom styling)
-Fetch API
-Backend
-FastAPI
-Pydantic
-Python
-AI Agent Logic
-Tool-based orchestration
-Modular agent flow (Log → Analyze → Act)

## 🧩 AI Agent Tools Implemented

-The agent uses multiple tools to handle CRM tasks:
  1.Log Interaction Tool
    Stores doctor interaction details securely.
  2.Edit Interaction Tool
    Allows updating incorrect or incomplete entries.
  3.Summarization Tool
    Converts raw notes into concise summaries.
  4.Classification Tool
    Categorizes interaction intent (Follow-up, Sales, Feedback, etc.).
  5.Follow-up Generator Tool
    Generates intelligent next-step actions based on interaction data.

## 🔁 Agent Workflow

User Input
   ↓
Log Interaction
   ↓
Summarize Notes
   ↓
Classify Interaction
   ↓
Generate Follow-up
   ↓
Final Output

-This mirrors real-world AI agent pipelines used in production systems.

## 🖥️ Application Features

-Clean and responsive UI
-Real-time AI agent execution
-FastAPI Swagger documentation
-Modular and scalable codebase
-Easy to extend with new tools

## 🚀 How to Run the Project

-Backend
   cd backend
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn main:app --reload
 Backend runs at:
👉 http://127.0.0.1:8000

-Frontend
    cd frontend
    npm install
    npm start
 Frontend runs at:
👉 http://localhost:3000

## 📸 Screenshots

🔹 AI Agent Output
![Agent Output](screenshots/agent-output.png)

🔹 FastAPI Swagger UI
![Swagger](screenshots/swagger.png)

## 🎯 Use Cases

-Healthcare CRM automation
-AI agent experimentation
-Tool-based AI workflows
-Full-stack AI application demo

## 📌 Why This Project Matters

-This project showcases:
   1.Practical AI agent design
   2.Clean frontend-backend integration
   3.Real-world automation thinking
   4.Industry-relevant architecture
-It’s not just a demo — it’s how modern AI systems are built.

## 👩‍💻 Author

Kalyani Varpe
Computer Engineering (3rd Year)
AI & Full-Stack Development Enthusiast
    


