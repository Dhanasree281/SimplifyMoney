import random

def detect_gold_query(query: str) -> bool:
    keywords = [
        "gold", "digital gold", "buy gold", "invest in gold",
        "gold price", "gold investment", "24k", "sovereign gold bond"
    ]
    text = query.lower()
    return any(k in text for k in keywords)

def generate_gold_fact() -> str:
    facts = [
        "Gold has historically acted as a hedge against inflation.",
        "Digital gold lets you buy 24k gold online without storage hassles.",
        "Gold prices often move inversely to risk assets during stress.",
        "Even small SIP-style amounts can accumulate into meaningful gold holdings.",
        "Always consider costs and storage/insurance when comparing gold products."
    ]
    return random.choice(facts)
