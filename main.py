import nextcord
from nextcord.ext import commands
import os

# Bật intents
intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot đã đăng nhập: {bot.user}")

# Slash command
@bot.slash_command(name="hello", description="Chào người dùng")
async def hello(interaction: nextcord.Interaction):
    await interaction.response.send_message(f"Xin chào {interaction.user.mention}!")

# Lấy token từ biến môi trường Railway
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
