from disnake import Embed, CommandInteraction, ui, SelectOption, __version__
from disnake.ext import commands

from datetime import datetime, timedelta
from _version import __bversion__
from time import time


class SlashUser(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.start_time = time()

    @commands.slash_command(name='info', description='Send information about bot')
    async def _info(self, inter: CommandInteraction):
        current_time = time()
        difference = int(round(current_time - self.start_time))
        uptime = str(timedelta(seconds=difference))

        infoEmbed = Embed(title='Information about bot',
                          color=0xb49dd4,
                          timestamp=datetime.utcnow())

        infoEmbed.set_author(name=f'Debilos Network Unified Server Ban List',
                             icon_url=f'{self.bot.user.display_avatar}')
        infoEmbed.set_footer(text='Copyright © Debilos Network 2022')
        infoEmbed.add_field(name='Author', value='OctoBanon')
        infoEmbed.add_field(name='Uptime', value=f'{uptime}')
        infoEmbed.add_field(name='Version', value=f'{__bversion__}')
        infoEmbed.add_field(name='Library', value=f'Disnake v{__version__}')
        infoEmbed.add_field(name='Last base update', value='#')
        await inter.response.send_message(embed=infoEmbed)

    @commands.slash_command(name='help', description='List of all bot commands')
    async def _help(self, inter: CommandInteraction):
        helpEmbed = Embed(title='Commands list',
                          description='Hello, you called help command, all the bot commands will be here',
                          color=0xb49dd4,
                          timestamp=datetime.utcnow())

        helpEmbed.set_author(name=f'Debilos Network Unified Server Ban List',
                             icon_url=f'{self.bot.user.display_avatar}')
        helpEmbed.set_footer(text='Copyright © Debilos Network 2022')

        await inter.response.send_message(
            embed=helpEmbed,
            components=ui.Select(options=[
                SelectOption(
                    label='User commands', description='Commands available to all', emoji='🔓'
                ),
                SelectOption(
                    label='Server owner commands', description='Commands for bot control', emoji='🔐'
                )
            ])
        )


def setup(bot):
    bot.add_cog(SlashUser(bot))
