import discord
from discord import app_commands
from discord.ext import commands

from bot import VerificationBot
from .utils.checks import bot_owner_or_admin
from .captcha.generate import create_captcha

class VerificationCog(commands.GroupCog):
    
    def __init__(self, bot: VerificationBot) -> None:
        self.bot = bot
    
    @app_commands.command()
    @app_commands.guild_only()
    @bot_owner_or_admin()
    async def channel(self, inter: discord.Interaction, channel: discord.TextChannel):
        ...
        
    @app_commands.command()
    async def test(self, inter: discord.Interaction):
        await inter.response.send_message(file=discord.File("", "captcha.png"))
        
async def setup(bot: VerificationBot) -> None:
    await bot.add_cog(VerificationCog(bot))