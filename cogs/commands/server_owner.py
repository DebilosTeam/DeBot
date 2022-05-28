from disnake.ext import commands
from disnake import Embed

from json import dump, load
from datetime import datetime


class SOCmd(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def activate(self, ctx):
        activateEmbed = Embed(title='Bot configuration',
                              description='Unified server ban list activated',
                              timestamp=datetime.now(),
                              color=0xb49dd4)
        activateEmbed.set_author(name=f'Debilos Network Unified Server Ban List',
                                 icon_url=f'{self.bot.user.display_avatar}')

        await ctx.send(embed=activateEmbed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def deactivate(self, ctx):
        deactivateEmbed = Embed(title='Bot configuration',
                                description='Unified server ban list deactivated',
                                timestamp=datetime.now(),
                                color=0xb49dd4)
        deactivateEmbed.set_author(name=f'Debilos Network Unified Server Ban List',
                                   icon_url=f'{self.bot.user.display_avatar}')

        await ctx.send(embed=deactivateEmbed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix):
        setPrefixEmbed = Embed(title='Bot configuration',
                               description=f'Bot server prefix is now `{prefix}`',
                               color=0xb49dd4,
                               timestamp=datetime.utcnow())
        setPrefixEmbed.set_author(name=f'Debilos Network Unified Server Ban List',
                                  icon_url=f'{self.bot.user.display_avatar}')

        with open('prefixes.json', 'r') as json_file:
            prefixes = load(json_file)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as json_file:
            dump(prefixes, json_file, indent=4)

        await ctx.send(embed=setPrefixEmbed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def setlang(self, ctx, lang: str):
        if lang == 'en':
            await ctx.send('English')
        elif lang == 'ru':
            await ctx.send('Русский')
        elif lang == 'ua':
            await ctx.send('Український')


def setup(bot):
    bot.add_cog(SOCmd(bot))
