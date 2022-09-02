from disnake.ext import commands
from disnake import Embed, Localized, Guild, OptionChoice


class UBLGuildControl(commands.Cog):
    def __init__(self, bot):
        """Its cog for ubl command guild_control and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description=Localized(key='UBL_GUILD_CONTROL_COMMAND_DESCRIPTION'))
    async def ubl_guild_control(self,
                                inter,
                                guild: Guild,
                                option: str = commands.Param(
                                    choices=[
                                        OptionChoice(name='ban', value='ban'),
                                        OptionChoice(name='unban', value='unban'),
                                    ]
                                )):
        moderators_records = await self.bot.db.fetch('SELECT * FROM ubl_moderators;')
        converted_records = [list(ids) for ids in moderators_records]
        ids_list = [ids for modlist in converted_records for ids in modlist]
        for ids in ids_list:
            if ids != inter.author.id:
                await inter.response.send_message('You are not moderator or bot owner')
                return

        if 981080304905244682 != inter.author.id:
            await inter.response.send_message('You are not moderator or bot owner')
            return

        if option == 'ban':
            ban_embed = Embed(
                title='UBL Guild Control',
                description='Guild successfully banned in UBL',
                color=0xb49dd4)
            ban_embed.add_field(name='Moderator', value=inter.author.display_name)
            ban_embed.add_field(name='Banned guild', value=guild.name + f' ({guild.id})')
            await inter.response.send_message(embed=ban_embed)
            # await self.bot.db.execute('')
        elif option == 'unban':
            unban_embed = Embed(
                title='UBL Guild Control',
                description='Guild successfully unbanned in UBL',
                color=0xb49dd4)
            unban_embed.add_field(name='Moderator', value=inter.author.display_name)
            unban_embed.add_field(name='Unbanned guild', value=guild.name + f' ({guild.id})')
            await inter.response.send_message(embed=unban_embed)


def setup(bot):
    bot.add_cog(UBLGuildControl(bot))
