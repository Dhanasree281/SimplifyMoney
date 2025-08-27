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

---
Out of curiosity i just want to add fronted part to the assessement using AI tools.
so the final result is this:
https://claude.ai/public/artifacts/25234189-6fb9-4911-b50e-6b3df2cd7464

