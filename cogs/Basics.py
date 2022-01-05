import discord, os, random, requests, json
from discord import File, Embed, channel
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
        """Check my latency"""
        await ctx.send(f'My ping is {self.bot.latency * 100} s!')

    @commands.command()
    async def hug(self, ctx, name: str = None):
        """I give users a hug"""
        name = name or ctx.author.name
        await ctx.send(f"I give a hug to {name}!")

    @commands.command()
    async def eightball(self, ctx):
        """I predict the future"""
        output = ["Yes", "No", "Unsure", "Can't answer right now"]
        await ctx.send(output[random.randint(0, len(output))])

    @commands.command()
    async def echo(self, ctx, *args):
        """I repeat what you say"""
        await ctx.send(' '.join(ctx.message.content.split()[1:]))
        await ctx.message.delete()

    @commands.command()
    async def advice(self, ctx):
        """I give advice from Zen Quotes"""
        advice = get_quote()
        await ctx.send(advice)

    @commands.command()
    async def stats(self, ctx):
        """Check out my stats"""
        embed = Embed(title="Stats", description="Here's my stats:")
        embed.add_field(name="Operating System", value="Ubuntu 20.04", inline=False)
        embed.add_field(name="Status", value="online and working", inline=False)
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


def setup(bot):
    bot.add_cog(Basics(bot))