import aiosqlite
import datetime

DB_NAME = "kuberai.db"

# ✅ Initialize DB with a purchases table
async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                amount REAL NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        await db.commit()

# ✅ Save purchase into DB
async def save_purchase(user_id: str, amount: float):
    async with aiosqlite.connect(DB_NAME) as db:
        timestamp = datetime.datetime.now().isoformat()
        await db.execute(
            "INSERT INTO purchases (user_id, amount, timestamp) VALUES (?, ?, ?)",
            (user_id, amount, timestamp)
        )
        await db.commit()
    return f"Purchase successful! {amount} INR of digital gold bought."

# ✅ Fetch all purchases for a given user
async def get_purchases(user_id: str):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT amount, timestamp FROM purchases WHERE user_id = ?",
            (user_id,)
        )
        rows = await cursor.fetchall()
        return [{"amount": row[0], "timestamp": row[1]} for row in rows]
