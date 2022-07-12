from disnake import Embed, __version__
from disnake.ext import commands

from datetime import datetime, timedelta
from time import time


class Info(commands.Cog):
    def __init__(self, bot):
        ```Help cog init```
        self.bot: commands.Bot = bot
        self.start_time = time()

    @commands.command(name='info')
    async def info(self, ctx):
        current_time = time()
        difference = int(round(current_time - self.start_time))
        uptime = str(timedelta(seconds=difference))

        infoembed = Embed(title='Information about bot',
                          color=0xb49dd4,
                          timestamp=datetime.utcnow())

        infoembed.set_author(name=f'{self.bot.user.name}',
                             icon_url=f'{self.bot.user.display_avatar}')
        infoembed.set_footer(text='Copyright © Debilos Team 2022')
        infoembed.add_field(name='Author', value='Debilos Team')
        infoembed.add_field(name='Uptime', value=f'{uptime}')
        infoembed.add_field(name='Version', value='Beta u14 (Sunrise)')
        infoembed.add_field(name='Library', value=f'Disnake v{__version__}')
        await ctx.send(embed=infoembed)


def setup(bot):
    bot.add_cog(Info(bot))
