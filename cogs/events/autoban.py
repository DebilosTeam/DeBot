from disnake.ext import commands


class Autoban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     print(message.content)


def setup(bot):
    bot.add_cog(Autoban(bot))
