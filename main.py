# main.py
import os
import nextcord
from flask import Flask
from threading import Thread

# ----------------------------
# Keep-alive server (Render cần cái này để không ngủ)
# ----------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot đang chạy 24/24 trên Render!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ----------------------------
# Bot setup
# ----------------------------
intents = nextcord.Intents.default()
client = nextcord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Đăng nhập thành công: {client.user}")
    await client.change_presence(
        status=nextcord.Status.online,
        activity=nextcord.Game("/hello")
    )

@client.slash_command(name="hello", description="Chào bot 👋")
async def hello(interaction: nextcord.Interaction):
    await interaction.response.send_message(f"👋 Xin chào {interaction.user.display_name}!", ephemeral=True)

# ----------------------------
# Run bot
# ----------------------------
keep_alive()  # bật web giữ online
client.run(os.getenv("MTQxOTIzNzg4MTkzMDU4NDEwNg.Gqwd-g.cvNxHIE1sJpIerdrML6pyGGOFND-zUxeoG-CzQ"))  # TOKEN để trong biến môi trường Render
