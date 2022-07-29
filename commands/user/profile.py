from disnake.ext import commands


class Profile(commands.Cog):
    def __init__(self, bot):
        """Its cog for user command profile and can't be used in another cogs or main.py"""
        self.bot = bot


def setup(bot):
    bot.add_cog(Profile(bot))
