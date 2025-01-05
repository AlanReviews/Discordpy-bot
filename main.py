import discord, os, asyncio, logging
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DESCRIPTION = '''Hello, I am Tara. I am a custom discord.py bot created by Alan.'''

intents = discord.Intents.default()
intents.message_content = True

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX", default="!!")
activity = discord.Game(name="Bonjour!")

ENVIRONMENT = os.getenv("ENVIRONMENT", default="development")

if ENVIRONMENT == "production":
    handler = logging.StreamHandler()
else:
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

logging.basicConfig(level=logging.DEBUG, handlers=[handler])

# subclassing commands.Bot
class MyBot(commands.Bot):
    # overriding setup_hook and doing our stuff in it
    async def setup_hook(self):
        print(f"Logging in as: {self.user}")
        initial_extensions = []
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                initial_extensions.append("cogs." + filename[:-3])
        
        for extension in initial_extensions:
            await bot.load_extension(extension)

bot = MyBot(command_prefix=commands.when_mentioned_or(PREFIX), description=DESCRIPTION, intents=intents, activity=activity, status=discord.Status.online)

@bot.event
async def on_message(message):
    await bot.process_commands(message)

bot.run(TOKEN)
