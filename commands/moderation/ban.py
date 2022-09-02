from disnake.ext import commands
from disnake import Member, Embed, Localized

from datetime import datetime


class Ban(commands.Cog):
    def __init__(self, bot):
        """Its cog for moderation command ban and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description=Localized(key='BAN_COMMAND_DESCRIPTION'))
    @commands.has_permissions(ban_members=True)
    async def ban(self, inter, member: Member, *, reason=None):
        if reason is None:
            reason = 'Not provided'

        embed = Embed(title='Member banned',
                      description='Member successfully banned on guild',
                      color=0xb49dd4)
        embed.add_field(name='Banned member', value=f'{member.display_name}')
        embed.add_field(name='Moderator', value=f'{inter.author.display_name}')
        embed.add_field(name='Reason', value=f'{reason}')

        await member.ban(reason=reason)
        await inter.response.send_message(embed=embed)

    @ban.error
    async def ban_perms_error(self, inter, error):
        if isinstance(error, commands.MissingPermissions):
            missing_permissions_embed = Embed(
                title="Warning",
                description="You are missing permission to run this command!",
                timestamp=datetime.utcnow(),
                color=0xb85667
            )
            await inter.response.send_message(embed=missing_permissions_embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Ban(bot))
