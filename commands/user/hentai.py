from disnake import Embed
from disnake.ext import commands

from datetime import datetime as dt
from requests import get


class Neko(commands.Cog):
    def __init__(self, bot):
        """Its cog for user command hentai and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description='Send random hentai art from selected category (NSFW)')
    @commands.is_nsfw()
    async def hentai(self, inter):
        r = get("https://nekobot.xyz/api/image?type=hneko")
        res = r.json()
        image = res['message']
        await inter.response.send_message(image)

    @hentai.error
    async def is_nsfw_error(self, inter, error):
        if isinstance(error, commands.NSFWChannelRequired):
            is_nsfw_error_embed = Embed(
                title="Warning",
                description="This command can be used only in NSFW marked channel",
                timestamp=dt.utcnow(),
                color=0x66b967
            )
            await inter.response.send_message(embed=is_nsfw_error_embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Neko(bot))
