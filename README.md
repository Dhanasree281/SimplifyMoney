# 💰 KuberAI – Digital Gold Assistant  

## 📌 Problem Statement  
Investing in **digital gold** is becoming popular, but many users:  
- Lack knowledge about how digital gold works  
- Struggle to simulate safe purchase transactions  
- Don’t have a simple API-based system to track purchases  

**Objective:**  
Build a backend system that:  
- Uses **AI logic / LLMs** to answer gold investment queries  
- Simulates digital gold purchases  
- Tracks transactions for each user  
- Provides easy-to-test APIs with Swagger UI  

**Goal:**  
Provide an **AI-powered backend assistant** to simplify learning and transacting in digital gold.  

---

## 🔍 Approach  
1. **AI Query Detection**  
   - Identify if a user’s query is related to digital gold  
   - Respond with useful investment facts (extendable to real LLMs like OpenAI)  

2. **Transaction Simulation**  
   - Allow users to "purchase" gold with an amount  
   - Store transactions in a mock database  

3. **Transaction History API**  
   - Retrieve all purchases by user ID  

4. **Interactive API Documentation**  
   - Swagger UI & ReDoc for easy testing  

---

## 📂 Project Workflow  
```mermaid
flowchart TD
    A[User Query / API Request] --> B[FastAPI Backend]
    B --> C[AI Logic: Detect Gold Query & Generate Fact]
    C --> D[Purchase Simulation]
    D --> E[Save to Mock Database]
    E --> F[Transaction History API]
    F --> G[Insights & Future Integration with LLMs]
#**⚡ Tech Stack**

Backend: FastAPI (Python)

Database: In-memory / SQLite (mock DB)

AI Logic: Rule-based (extendable to LLMs like OpenAI/Anthropic)

Docs: Swagger UI, ReDoc
🔗 API Endpoints
1️⃣ Ask a Question
POST /ask-question


Request:

{ "query": "Tell me about digital gold" }


Response:

{
  "response": "Digital gold lets you buy 24k gold online without storage hassles.",
  "action": "Would you like to purchase digital gold?",
  "next_endpoint": "/purchase-gold"
}

2️⃣ Purchase Gold
POST /purchase-gold


Request:

{ "user_id": "user123", "amount": 100 }


Response:

{ "status": "success", "message": "Purchase of 100 units saved for user123" }

3️⃣ View Transactions
GET /transactions/{user_id}


Response:

{
  "user_id": "user123",
  "transactions": [
    { "amount": 100, "timestamp": "2025-08-26T20:18:33.127068" }
  ]
}

🚀 Setup Instructions

Clone the repo:

git clone https://github.com/<your-username>/kuberai-assignment.git
cd kuberai-assignment


Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Run FastAPI server:

uvicorn main:app --reload

📌 Future Enhancements

Integrate real LLMs (OpenAI/Anthropic) for dynamic AI answers

Use persistent DB (Postgres/SQLite) instead of mock DB

Build frontend UI (React/Next.js) for smooth user interaction

👩‍💻 Author

Your Name

🌐 LinkedIn
 | GitHub


---

👉 This version matches the **style of your sales analysis README** (Problem Statement → Approach → Workflow → APIs → Setup → Future Enhancements).  

Do you want me to also generate a **matching `requirements.txt`** so your repo looks 100% complete and professional?
