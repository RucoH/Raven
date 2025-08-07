import os
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Konfigürasyon
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX", "!")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# Cog'ları yükleyeceğimiz yer
initial_cogs = [
    "cogs.entertainment",
    "cogs.music",
]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    for cog in initial_cogs:
        try:
            bot.load_extension(cog)
            logging.info(f"Loaded cog: {cog}")
        except Exception as e:
            logging.error(f"Failed to load cog {cog}: {e}")
    bot.run(TOKEN)
