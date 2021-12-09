import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DESCRIPTION = '''Hello, I am Tara. I am a custom discord.py bot.'''

intents = discord.Intents.default()
intents.members = True

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!!', description=DESCRIPTION, intents=intents)

@bot.event
async def on_ready():
    game = discord.Game("!!help | Dancing")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(TOKEN)
