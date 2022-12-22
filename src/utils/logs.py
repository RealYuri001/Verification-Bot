from dataclasses import dataclass

import discord

@dataclass
class Modlogs:
    _id: int
    affected_user: discord.User
    responsible_mod: discord.Member
    guild: discord.Guild
    channel: discord.abc.GuildChannel
    reason: str
    
    def to_dict(self) -> dict:
        return {
            "_id": self._id,
            "affected_user": self.affected_user,
            "responsible_mod": self.responsible_mod,
            "channel": self.channel,
            "reason": self.reason,
            "guild": self.guild,
        }