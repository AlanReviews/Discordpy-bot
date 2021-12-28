import discord, os, random, requests, json
from discord import channel
from discord.ext import commands
from discord import Embed, Member
from typing import Optional

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        embed = Embed(title="Server information")
        fields = [("ID", ctx.guild.id, True), ("Creation date", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, user: discord.User = None):
        if user is None:
            user = ctx.author
        embed = Embed(title="User information", colour=user.colour)
        embed.set_thumbnail(url=user.avatar)
        fields = [("ID", user.id, False), ("Name", str(user), True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(moderation(bot))