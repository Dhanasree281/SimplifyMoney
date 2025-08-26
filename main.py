from fastapi import FastAPI
from models import AskRequest, PurchaseRequest
from ai_logic import detect_gold_query, generate_gold_fact
from database import init_db, save_purchase, get_purchases  # add get_purchases here


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.post("/ask-question")
async def ask_question(req: AskRequest):
    if detect_gold_query(req.query):
        fact = generate_gold_fact()
        return {
            "response": fact,
            "action": "Would you like to purchase digital gold?",
            "next_endpoint": "/purchase-gold"
        }
    else:
        return {"response": "Sorry, I can only help with gold investment-related queries."}

@app.post("/purchase-gold")
async def purchase_gold(req: PurchaseRequest):
    result = await save_purchase(req.user_id, req.amount)
    return {"status": "success", "message": result}

@app.get("/transactions/{user_id}")
async def transactions(user_id: str):
    purchases = await get_purchases(user_id)
    return {"user_id": user_id, "transactions": purchases}


from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
    <head>
        <title>KuberAI Backend</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Inter', sans-serif;
                background: linear-gradient(to right, #eef2f3, #8e9eab);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: #333;
            }

            .card {
                background-color: #ffffff;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 500px;
                width: 90%;
            }

            .logo {
                width: 80px;
                height: 80px;
                border-radius: 50%;
                margin-bottom: 20px;
            }

            h1 {
                color: #007acc;
                margin-bottom: 10px;
            }

            h2 {
                font-weight: 400;
                font-size: 1.1rem;
                color: #555;
                margin-bottom: 20px;
            }

            .button {
                display: inline-block;
                margin: 10px;
                padding: 12px 24px;
                font-size: 1rem;
                color: white;
                background-color: #007acc;
                border: none;
                border-radius: 8px;
                text-decoration: none;
                transition: background-color 0.3s ease, transform 0.2s;
            }

            .button:hover {
                background-color: #005fa3;
                transform: translateY(-2px);
            }

            .footer {
                margin-top: 30px;
                font-size: 0.95rem;
                color: #666;
            }

            .footer a {
                text-decoration: none;
                color: #007acc;
                margin: 0 8px;
                font-weight: bold;
            }

            .footer a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <img src="https://iili.io/KdLbm1s.md.jpg" class="logo" alt="Simplify Money Logo">
            <h1>✅ KuberAI Backend</h1>
           
            <p>Interact with the AI API using the buttons below:</p>
            <a href="/docs" class="button">📘 Swagger UI</a>
            <a href="/redoc" class="button">📙 ReDoc</a>

            <div class="footer">
                <p>💼 Connect with me:</p>
                <a href="https://github.com/Dhanasree281" target="_blank">GitHub</a> |
                <a href="https://www.linkedin.com/in/dhanasree-danda/" target="_blank">LinkedIn</a>
            </div>
        </div>
    </body>
    </html>
    """
