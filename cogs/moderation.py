import discord
from discord import channel
from discord.ext import commands
from discord import Embed, member
from discord.ext.commands import has_permissions, MissingPermissions
from typing import Optional
import logging

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        """Shows server information in an embed"""
        logging.info(f"Serverinfo command invoked by {ctx.author}")
        embed = Embed(title="Server information")
        embed.set_thumbnail(url = ctx.guild.icon)
        fields = [("Name", ctx.guild.name, True), ("ID", ctx.guild.id, True), ("Creation date", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),("Member count", ctx.guild.member_count, True),
        ("Explicit content filer", ctx.guild.explicit_content_filter, True), ("Verification level", ctx.guild.verification_level, True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, user: discord.User = None):
        """Shows user information and their avatar in an embed"""
        if user is None:
            user = ctx.author
        logging.info(f"Userinfo command invoked by {ctx.author} for {user}")
        embed = Embed(title="User information", colour=user.colour)
        embed.set_thumbnail(url=user.display_avatar)
        fields = [("Name", str(user), False), ("ID", user.id, False), ("System", user.system, False), ("Bot", user.bot, False)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, reason = "not specified"):
        """Removes a member from the server. The member can rejoin that server. Only members with the kick members permission can use this command."""
        logging.info(f"Kick command invoked by {ctx.author} for {member} with reason {reason}")
        await member.send("You got kicked for " + reason)
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked!')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, reason = "not specified"):
        """Removes a member from a server. The member cannot rejoin the server until the member gets unbanned. Only members with the ban members permission can use this command."""
        logging.info(f"Ban command invoked by {ctx.author} for {member} with reason {reason}")
        try:
            await member.send("You got banned for " + reason)
            await member.ban(delete_message_days=7, reason=reason)
        except Exception as e:
            logging.error(f"Error banning user {member}: {e}")
            return await ctx.send(e)
        await ctx.send(f'User {member} got banned!')

async def setup(bot):
    await bot.add_cog(moderation(bot))
