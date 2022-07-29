from disnake.ext import commands
from disnake import Activity, ActivityType

from main import get_config


class ReadyEvent(commands.Cog):
    def __init__(self, bot):
        """Its cog for event ready created only for on_ready listener"""
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"The bot is ready.\n"
            f"User: {self.bot.user}\n"
            f"ID: {self.bot.user.id}"
        )
        await self.bot.change_presence(activity=Activity(type=get_config()['type'],
                                                         name=get_config()['name'],
                                                         url=get_config()['twitch_url']))


def setup(bot):
    bot.add_cog(ReadyEvent(bot))
