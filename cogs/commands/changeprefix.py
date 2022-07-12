from disnake import Embed
from disnake.ext import commands

from datetime import datetime


class ChangePrefix(commands.Cog):
    def __init__(self, bot):
        ```Help cog init```
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix):
        setprefixembed = Embed(title='Bot configuration',
                               description=f'Bot server prefix is now `{prefix}`',
                               color=0xb49dd4,
                               timestamp=datetime.utcnow())

        await self.bot.db.execute('UPDATE guild_configuration SET prefix = $1 WHERE "id" = $2', prefix, ctx.guild.id)

        await ctx.send(embed=setprefixembed)


def setup(bot):
    bot.add_cog(ChangePrefix(bot))
