from disnake.ext import commands
from disnake import Member, Embed, Localized

from datetime import datetime


class Kick(commands.Cog):
    def __init__(self, bot):
        """Its cog for moderation command kick and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description=Localized(key='KICK_COMMAND_DESCRIPTION'))
    @commands.has_permissions(kick_members=True)
    async def kick(self, inter, member: Member, *, reason=None):
        if reason is None:
            reason = 'Not provided'

        embed = Embed(title='Member kicked',
                      description='Member successfully kicked from guild',
                      color=0xb49dd4)
        embed.add_field(name='Kicked member', value=f'{member.display_name}')
        embed.add_field(name='Moderator', value=f'{inter.author.display_name}')
        embed.add_field(name='Reason', value=f'{reason}')

        await member.kick(reason=reason)
        await inter.response.send_message(embed=embed)

    @kick.error
    async def kick_perms_error(self, inter, error):
        if isinstance(error, commands.MissingPermissions):
            missing_permissions_embed = Embed(
                title="Warning",
                description="You are missing permission to run this command!",
                timestamp=datetime.utcnow(),
                color=0xb85667
            )
            await inter.response.send_message(embed=missing_permissions_embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Kick(bot))
