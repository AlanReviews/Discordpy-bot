import discord, os, random, requests, json
from discord.ext import commands

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")

class Basics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command
    @commands.command()
    async def ping(self, ctx, name: str = None):
        await ctx.send(f'My ping is {self.bot.latency} s!')

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

def setup(bot):
    bot.add_cog(Basics(bot))