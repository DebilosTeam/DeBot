from disnake import CommandInteraction, Embed
from disnake.ext import commands

from datetime import datetime


class SlashSOCmd(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.slash_command(name='activate', description='Activating of unified ban lists and auto ban system')
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def _activate(self, inter: CommandInteraction):
        activateEmbed = Embed(title='Bot configuration',
                              description='Unified server ban list activated',
                              timestamp=datetime.now(),
                              color=0xb49dd4)
        activateEmbed.set_author(name=f'Debilos Network Unified Server Ban List',
                                 icon_url=f'{self.bot.user.display_avatar}')

        await inter.response.send_message(embed=activateEmbed)

    @commands.slash_command(name='deactivate', description='Deactivating of unified ban lists and auto ban system')
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def _deactivate(self, inter: CommandInteraction):
        deactivateEmbed = Embed(title='Bot configuration',
                                description='Unified server ban list deactivated',
                                timestamp=datetime.now(),
                                color=0xb49dd4)
        deactivateEmbed.set_author(name=f'Debilos Network Unified Server Ban List',
                                   icon_url=f'{self.bot.user.display_avatar}')

        await inter.response.send_message(embed=deactivateEmbed)

    @commands.slash_command(name='setprefix', description='Setting local prefix in guild')
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def _setprefix(self, inter: CommandInteraction, prefix):
        setPrefixEmbed = Embed(title='Bot configuration',
                               description=f'Bot server prefix is now `{prefix}`',
                               color=0xb49dd4,
                               timestamp=datetime.utcnow())
        setPrefixEmbed.set_author(name=f'Debilos Network Unified Server Ban List',
                                  icon_url=f'{self.bot.user.display_avatar}')

        await self.bot.db.execute('UPDATE guild_prefixes SET prefix = $1 WHERE "id" = $2', prefix, inter.guild.id)

        await inter.response.send_message(embed=setPrefixEmbed)

    @commands.slash_command(name='setlang', description='Setting default language for guild')
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def _setlang(self, inter: CommandInteraction, lang: str):
        if lang == 'en':
            await inter.response.send_message('English')
        elif lang == 'ru':
            await inter.response.send_message('Русский')
        elif lang == 'ua':
            await inter.response.send_message('Український')
        else:
            await inter.response.send_message('Unknown language selected')


def setup(bot):
    bot.add_cog(SlashSOCmd(bot))
