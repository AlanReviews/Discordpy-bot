import discord, os, random, aiohttp, json
from discord import File, Embed, channel
from discord.ext import commands
import random

class Basics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Here's a list of basic commands I created
    @commands.command()
    async def ping(self, ctx, name: str = None):
        """Check my websocket latency"""
        await ctx.send(f'My ping is {round(self.bot.latency * 100,2)} ms!')

    @commands.command()
    async def hug(self, ctx, name: str = None):
        """I give users a hug"""
        name = name or ctx.author.name
        await ctx.send(f"I give a hug to {name}!")

    @commands.command()
    async def eightball(self, ctx, arg):
        """I predict the future"""
        output = ["Yes", "No", "Unsure", "Can't answer right now"]
        await ctx.send(output[random.randint(0, len(output))])

    @commands.command()
    async def echo(self, ctx, *args):
        """I repeat what you say"""
        await ctx.send(' '.join(ctx.message.content.split()[1:]))
        await ctx.message.delete()

    @commands.command()
    async def quote(self, ctx):
        """I give a quote from Zen Quotes"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://zenquotes.io/api/random") as r:
                res = await r.json()  # returns dict
                quote = res[0]['q'] + " -" + res[0]['a']
                await ctx.send(quote)
    
    @commands.command()
    async def stats(self, ctx):
        """Check out my stats"""
        total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])
        memory_usage = round((used_memory/total_memory) * 100, 2)
        embed = Embed(title="Stats", description="Here's my stats:")
        embed.add_field(name="Operating System", value="Ubuntu 20.04", inline=False)
        embed.add_field(name="Status", value="online and working", inline=False)
        embed.add_field(name="Memory usage (%)", value=memory_usage, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def ubuntu(self, ctx):
        """Shows Ubuntu logo in ASCII format"""
        await ctx.send(file=File(fp="cogs/Ubuntu.png"))
    
    @commands.command(name='roll', aliases=['dice'])
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)
        
    @commands.command(name='choose', description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))
        
    @commands.command(name='dm')
    async def dm(self, ctx):
        """Sends a hello in dms"""
        try:
            await ctx.message.author.send("Hello there")
        except:
            await ctx.send("Hey! I cannot dm you.")

    @commands.command(name='faq', aliases=["questions"])
    async def faq(self, ctx):
        """Sends you a link to the Alan Reviews FAQ page"""
        await ctx.send("What does Alan review? How do I request a video review? All the answers are in this link: https://principled-lychee-346.notion.site/12bf6d65f1d74780937fa8ae3ed70fe4?v=fd59a2938e614e988fdcb69914306633 You're welcome.")

    @commands.command(name='links', aliases=['link'])
    async def links(self, ctx):
        """Lists all my important links in an embed."""
        links = discord.Embed(title="List of Links",description="Here is a list of links. More will be added later. Enjoy!",colour=0xFF0000)
        links.set_author(name="Alan")
        links.add_field(name="YouTube", value="https://www.youtube.com/c/TheAlanReviews", inline=False)
        links.add_field(name="Frequently asked questions", value="https://principled-lychee-346.notion.site/12bf6d65f1d74780937fa8ae3ed70fe4?v=fd59a2938e614e988fdcb69914306633", inline=False)
        links.add_field(name="Review list", value="https://docs.google.com/spreadsheets/d/1FbS8VpjTf0l9czePzXDp3A89EEW3U43-qVpyjDyFMq4/edit?usp=sharing", inline=False)
        links.add_field(name="GitHub Repository", value="https://github.com/AlanReviews/Discordpy-bot", inline=False)
        await ctx.send(embed=links)


def setup(bot):
    bot.add_cog(Basics(bot))