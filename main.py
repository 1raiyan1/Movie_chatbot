import aiosqlite
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()
async def init_db():
    async with aiosqlite.connect("chat_history.db") as db:
        await db.execute(
            """CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                message TEXT
            )"""
        )
        await db.commit()

@app.on_event("startup")
async def startup():
    await init_db()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    user_id = websocket.client.host  
    
    async with aiosqlite.connect("chat_history.db") as db:
        async with db.execute("SELECT message FROM chat_history WHERE user_id = ?", (user_id,)) as cursor:
            messages = await cursor.fetchall()
            for message in messages:
                await websocket.send_text(message[0])

    try:
        while True:
            data = await websocket.receive_text()
            async with aiosqlite.connect("chat_history.db") as db:
                await db.execute("INSERT INTO chat_history (user_id, message) VALUES (?, ?)", (user_id, data))
                await db.commit()
            
            await websocket.send_text(f"Bot: {data}")
    except WebSocketDisconnect:
        print(f"User {user_id} disconnected")
