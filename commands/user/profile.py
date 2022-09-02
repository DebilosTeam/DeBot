from disnake import Embed, Member
from disnake.ext import commands

from datetime import datetime


class Profile(commands.Cog):
    def __init__(self, bot):
        """Its cog for user command profile and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description='User profile')
    async def profile(self, inter, *, member: Member = None):
        badges = '\u200b'
        if member is None:
            member = inter.author

        moderators_records = await self.bot.db.fetch('SELECT * FROM ubl_moderators;')
        converted_records = [list(ids) for ids in moderators_records]
        ids_list = [ids for modlist in converted_records for ids in modlist]
        for ids in ids_list:
            if member.id == ids:
                badges = ':hammer:'

        profile_embed = Embed(
            title='User profile',
            color=0xb49dd4)
        profile_embed.set_thumbnail(url=member.avatar.url)
        profile_embed.add_field(name='Username', value=f'{member.display_name}')
        profile_embed.add_field(name='ID', value='#')
        profile_embed.add_field(name='Badges', value=f'{badges}')
        await inter.response.send_message(embed=profile_embed)


def setup(bot):
    bot.add_cog(Profile(bot))
    bot.loop.run_until_complete(bot.create_db_pool())

