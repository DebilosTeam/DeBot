from disnake.ext import commands
from disnake import Embed, __version__, Localized

from datetime import datetime
from datetime import timedelta
from time import time


class Info(commands.Cog):
    def __init__(self, bot):
        """Its cog for user command info and can't be used in another cogs or main.py"""
        self.bot = bot
        self.start_time = time()

    @commands.slash_command(name='info', description=Localized(key='INFO_COMMAND_DESCRIPTION'))
    async def info(self, inter):
        current_time = time()
        difference = int(round(current_time - self.start_time))
        uptime = str(timedelta(seconds=difference))

        embed = Embed(title='Information about bot',
                           color=0xb49dd4,
                           timestamp=datetime.utcnow())
        embed.set_author(name=f'{self.bot.user.name}',
                              icon_url=f'{self.bot.user.display_avatar}')
        embed.set_footer(text='Copyright © Debilos Team 2022',
                              icon_url='https://gitlab.com/uploads/-/system/group/avatar/15944551/resized-image-Promo'
                                       '.jpeg?width=64')
        embed.add_field(name='Created by', value='Debilos Team')
        embed.add_field(name='Uptime', value=f'{uptime}')
        embed.add_field(name='Version', value='0.10.0')
        embed.add_field(name='Library', value=f'Disnake v{__version__}')
        await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
