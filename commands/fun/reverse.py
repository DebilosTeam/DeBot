from disnake.ext import commands
from disnake import Embed


class Reverse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Reverse entered text')
    async def reverse(self, inter, *, text):
        reverse_embed = Embed(
            title='Text reversing',
            color=0xb49dd4)
        reverse_embed.add_field(name='Original text:', value=text)
        reverse_embed.add_field(name='Reversed text:', value=text[::-1])
        await inter.response.send_message(embed=reverse_embed)



def setup(bot):
    bot.add_cog(Reverse(bot))
