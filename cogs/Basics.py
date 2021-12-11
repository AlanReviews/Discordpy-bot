import discord, os, random, requests, json
from discord.ext import commands

def get_quote():
    # Call a get request
    response = requests.get("https://zenquotes.io/api/random")
    # Extract the JSON Data
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

class Basics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Here's a list of basic commands I created
    @commands.command()
    async def ping(self, ctx, name: str = None):
        await ctx.send(f'My ping is {self.bot.latency * 100} s!')

    @commands.command()
    async def hug(self, ctx, name: str = None):
        name = name or ctx.author.name
        await ctx.send(f"I give a hug to {name}!")

    @commands.command()
    async def eightball(self, ctx):
        output = ["Yes", "No", "Unsure", "Can't answer right now"]
        await ctx.send(output[random.randint(0, len(output))])

    @commands.command()
    async def echo(self, ctx, *args):
        await ctx.send(' '.join(ctx.message.content.split()[1:]))
        await ctx.message.delete()

    @commands.command()
    async def advice(self, ctx):
        advice = get_quote()
        await ctx.send(advice)

def setup(bot):
    bot.add_cog(Basics(bot))