from typing import Callable, TypeVar

import discord
from discord import app_commands

T = TypeVar('T')

def bot_owner_or_admin() -> Callable[[T], T]:
    def pred(interaction: discord.Interaction) -> bool:
        perms = interaction.permissions.administrator
        
        if not perms:
            return False
        
        if interaction.user.id in interaction.client.owner_ids:
            return True
        
        return True
    
    return app_commands.check(pred)