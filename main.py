import discord, os, asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DESCRIPTION = '''Hello, I am Tara. I am a custom discord.py bot created by Alan.'''

intents = discord.Intents.default()
intents.members = True

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX", default="!!")
activity = discord.Game(name="!!help | Summertime!")

client = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), description=DESCRIPTION, intents=intents, activity=activity, status=discord.Status.online)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")

initial_extensions = []


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for extension in initial_extensions:
        client.load_extension(extension)

client.run(TOKEN)
