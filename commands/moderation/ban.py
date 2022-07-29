from disnake.ext import commands
from disnake import Member, Embed

from datetime import datetime


class Ban(commands.Cog):
    def __init__(self, bot):
        """Its cog for moderation command ban and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description='Ban member on server')
    @commands.has_permissions(ban_members=True)
    async def ban(self, inter, member: Member, *, reason=None):
        if reason is None:
            reason = "Not provided"

        await member.ban(reason=reason)
        await inter.response.send_message(f"{member} " + f"{reason}")

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
