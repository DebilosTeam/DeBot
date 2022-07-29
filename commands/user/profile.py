from disnake import Embed, Member
from disnake.ext import commands

from datetime import datetime as dt


class Profile(commands.Cog):
    def __init__(self, bot):
        """Its cog for user command profile and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description='User profile')
    async def profile(self, inter):
        profile_embed = Embed(
            title='User profile',
            color=0xb49dd4,
            timestamp=dt.utcnow()
        )
        profile_embed.set_thumbnail(url=inter.author.avatar)
        profile_embed.add_field(name='Username', value=f'{inter.author.name}')
        profile_embed.add_field(name='ID', value='#')
        profile_embed.add_field(name='Badges', value='#')
        await inter.response.send_message(embed=profile_embed)


def setup(bot):
    bot.add_cog(Profile(bot))
    bot.loop.run_until_complete(bot.create_db_pool())

