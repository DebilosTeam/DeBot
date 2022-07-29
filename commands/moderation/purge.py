from disnake.ext import commands
from disnake import Embed

from datetime import datetime


class Purge(commands.Cog):
    def __init__(self, bot):
        """Its cog for moderation command purge and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description='Remove one or multiple message(s)')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, inter, amount: int):
        success_embed = Embed(
            title='Cleaning...',
            description=f'Removed `{amount}` messages',
            color=0xb49dd4,
            timestamp=datetime.utcnow()
        )
        await inter.channel.purge(limit=amount)
        await inter.response.send_message(embed=success_embed)


def setup(bot):
    bot.add_cog(Purge(bot))
