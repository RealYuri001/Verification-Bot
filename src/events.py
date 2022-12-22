import discord
from discord.ext import commands

from bot import VerificationBot

class Events(commands.Cog):
    def __init__(self, bot: VerificationBot) -> None:
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        config = await self.bot.db.get()
    
async def setup(bot: VerificationBot) -> None:
    await bot.add_cog(Events(bot))