from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from Izumi.VideoStreaming import app


Misery = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Izumi"),
)

Misery.start()
print("[Your Izumi Is Ready To Stream✓")
app.start()
print("Started Successfully✓")
idle()
