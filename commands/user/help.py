from disnake.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        """Its cog for command help and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description='Send bot command list')
    async def help(self, inter):
        await inter.response.send_message("GG")


def setup(bot):
    bot.add_cog(Help(bot))
