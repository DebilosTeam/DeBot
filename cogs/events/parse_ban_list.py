from disnake.ext import commands
from disnake import Guild

from json import dump


class Parsebanlist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(self, guild: Guild, members):
        bans = [entry async for entry in guild.bans()]
        loop = [f"{u[1].id}" for u in bans]


def setup(bot):
    bot.add_cog(Parsebanlist(bot))
