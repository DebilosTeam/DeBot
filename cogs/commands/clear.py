from disnake.ext import commands
from disnake import Embed

from datetime import datetime


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = None):
        if amount is None:
            notsuccessembed = Embed(
                title='Error',
                description="You didn't enter the number of messages",
                color=0xb49dd4,
                timestamp=datetime.utcnow()
            )
            await ctx.send(embed=notsuccessembed)
            return
        else:
            successembed = Embed(
                title='Cleaning...',
                description=f'Removed `{amount}` messages',
                color=0xb49dd4,
                timestamp=datetime.utcnow()
            )
            await ctx.channel.purge(limit=amount+1)
            await ctx.send(embed=successembed)


def setup(bot):
    bot.add_cog(Clear(bot))
