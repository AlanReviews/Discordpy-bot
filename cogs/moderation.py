import discord, os, random, requests, json
from discord import channel
from discord.ext import commands
from discord import Embed, member
from discord.ext.commands import has_permissions, MissingPermissions
from typing import Optional

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        """Shows server information in an embed"""
        embed = Embed(title="Server information")
        fields = [("ID", ctx.guild.id, True), ("Creation date", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),("Member count", ctx.guild.member_count, True),
        ("Explicit content filer", ctx.guild.explicit_content_filter, True), ("Verification level", ctx.guild.verification_level, True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, user: discord.User = None):
        """Shows user information in an embed"""
        if user is None:
            user = ctx.author
        embed = Embed(title="User information", colour=user.colour)
        embed.set_thumbnail(url=user.display_avatar)
        fields = [("ID", user.id, False), ("Name", str(user), True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason):
        """Removes a member from the server. The member can rejoin that server. Only members with the kick members permission can use this command."""
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')
        await ctx.message.author.send(f'You got kicked for {reason}. Come back when you behave.')


async def setup(bot):
    await bot.add_cog(moderation(bot))