from disnake import Embed, __version__
from disnake.ext import commands

from datetime import datetime, timedelta
from time import time


class Info(commands.Cog):
    def __init__(self, bot):
        """Its cog for command info and can't be used in another cogs or main.py"""
        self.bot = bot
        self.start_time = time()

    @commands.slash_command(description='Send information about bot')
    async def info(self, inter):
        current_time = time()
        difference = int(round(current_time - self.start_time))
        uptime = str(timedelta(seconds=difference))

        info_embed = Embed(title='Information about bot',
                           color=0xb49dd4,
                           timestamp=datetime.utcnow())

        info_embed.set_author(name=f'{self.bot.user.name}',
                              icon_url=f'{self.bot.user.display_avatar}')
        info_embed.set_footer(text='Copyright © Debilos Team 2022')
        info_embed.add_field(name='Created by', value='Debilos Team')
        info_embed.add_field(name='Uptime', value=f'{uptime}')
        info_embed.add_field(name='Version', value='Beta u16 (Sunflower)')
        info_embed.add_field(name='Library', value=f'Disnake v{__version__}')
        await inter.response.send_message(embed=info_embed)


def setup(bot):
    bot.add_cog(Info(bot))
