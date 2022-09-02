from disnake.ext import commands
from disnake import Embed, Member, Localized


class Avatar(commands.Cog):
    def __init__(self, bot):
        """Its cog for user command avatar and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description=Localized(key='AVATAR_COMMAND_DESCRIPTION'))
    async def avatar(self, inter, user: Member):
        embed = Embed(
            title=str(user),
            color=0xb49dd4)
        embed.set_image(url=user.display_avatar.url)
        await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Avatar(bot))
