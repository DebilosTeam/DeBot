from disnake.ext import commands
from disnake import Member, Embed

from datetime import datetime


class Kick(commands.Cog):
    def __init__(self, bot):
        """Its cog for moderation command kick and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description='Kick member from server')
    @commands.has_permissions(kick_members=True)
    async def kick(self, inter, member: Member, *, reason=None):
        if reason is None:
            reason = "Not provided"

        await member.kick(reason=reason)
        await inter.response.send_message(f"{member} " + f"{reason}")

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
