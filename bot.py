import os
from typing import Any

import discord
from discord import app_commands
from discord.ext import commands
from redis import asyncio as aioredis
from redis.commands.json import JSON as ReJSON

intents = discord.Intents.default()
intents.message_content = True

class VerificationBot(commands.Bot):
    def __init__(self, **kwargs: Any):
        super().__init__(
            command_prefix=".", 
            intents=intents,
            owner_ids=[
                383764756202258436, 
                953750154303905822, 
                607197619193643029, 
                994830124165906444
            ], #Replace with your own ID. 
            **kwargs,
        )
        
        self.__db_base = aioredis.Redis()
        #Put your own link if you have one. I use localhost and it is not required.
    
    async def load_extensions(self, *name: str, package: str | None = None) -> None:
        for ext in name:
            await self.load_extension(ext, package=package)
    
    async def setup_hook(self) -> None:
        await self.load_extensions(*("src.verification", "src.events", "jishaku"))
    
    @property
    def db(self) -> ReJSON:
        return self.__db_base.json()

cli = VerificationBot()

if __name__ == '__main__':
    cli.run(os.getenv('token')) #Bot token here.