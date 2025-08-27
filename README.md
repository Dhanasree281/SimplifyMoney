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
## Demo Videos
**The Demo video of the actual project is attactched in above file:please go through it

## 🎨 Frontend Exploration with AI Tools

Out of curiosity, I also explored how the backend could look if extended with a **frontend interface** powered by AI tools.  
Instead of only JSON API responses, the idea was to create a **chatbot-style web page** where users can:

- Ask gold investment–related questions 💬  
- Get AI-generated answers ✨  
- Purchase digital gold via button clicks 🪙  
- View their past transactions 📜  

🚀 **Final Result (Demo):**  
👉 [Click here to view the prototype](https://claude.ai/public/artifacts/25234189-6fb9-4911-b50e-6b3df2cd7464)  




## 📂 Project Workflow  
```mermaid
flowchart TD
    A[User Query / API Request] --> B[FastAPI Backend]
    B --> C[AI Logic: Detect Gold Query & Generate Fact]
    C --> D[Purchase Simulation]
    D --> E[Save to Mock Database]
    E --> F[Transaction History API]
    F --> G[Insights & Future Integration with LLMs]
