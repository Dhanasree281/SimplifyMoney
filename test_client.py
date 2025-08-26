import requests

BASE_URL = "http://127.0.0.1:8000"

def step1_ask_question():
    print("\n👉 Step 1: Asking a question about gold investment...")
    payload = {"query": "Is digital gold a good investment?"}
    res = requests.post(f"{BASE_URL}/ask-question", json=payload)
    print("Response:", res.json())
    return res.json()

def step2_purchase_gold(user_id="user123", amount=100):
    print("\n👉 Step 2: Purchasing digital gold...")
    payload = {"user_id": user_id, "amount": amount}
    res = requests.post(f"{BASE_URL}/purchase-gold", json=payload)
    print("Response:", res.json())
    return res.json()

def step3_check_transactions(user_id="user123"):
    print("\n👉 Step 3: Checking transaction history...")
    res = requests.get(f"{BASE_URL}/transactions/{user_id}")
    print("Response:", res.json())
    return res.json()

if __name__ == "__main__":
    step1_ask_question()
    step2_purchase_gold()
    step3_check_transactions()
