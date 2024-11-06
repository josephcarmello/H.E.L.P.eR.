import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = disnake.Intents.default()
intents.message_content = True  # Enable if your bot needs message content access

bot = commands.Bot(command_prefix="!", intents=intents)

initial_extensions = ["cogs.general", "cogs.admin"]

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.event
async def on_error(event, *args, **kwargs):
    print(f"Error in event {event}: {args} {kwargs}")


if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)

# Start helper :)
bot.run(TOKEN)
