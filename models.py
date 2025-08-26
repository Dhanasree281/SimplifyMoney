from pydantic import BaseModel

class AskRequest(BaseModel):
    query: str

class PurchaseRequest(BaseModel):
    user_id: str
    amount: float
