import discord, os
from discord.ext import commands
import logging

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            logging.info(f"Member {member} joined the server")
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command(name='hello', aliases=['hi', 'hey'])
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            logging.info(f"Hello command invoked by {ctx.author} for {member}")
            await ctx.send('Hello {0.name}'.format(member))
        else:
            logging.info(f"Hello command invoked by {ctx.author} for {member} (familiar)")
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

async def setup(bot):
    await bot.add_cog(Greetings(bot))
