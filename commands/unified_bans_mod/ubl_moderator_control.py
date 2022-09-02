from disnake.ext import commands
from disnake import Embed, Localized, Member, OptionChoice


class UBLModeratorControl(commands.Cog):
    def __init__(self, bot):
        """Its cog for ubl command moderator_control and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description=Localized(key='UBL_MODERATOR_CONTROL_COMMAND_DESCRIPTION'))
    @commands.is_owner()
    async def ubl_moderator_control(self,
                                    inter,
                                    member: Member,
                                    option: str = commands.Param(
                                        choices=[
                                            OptionChoice(name='add', value='0'),
                                            OptionChoice(name='remove', value='1'),
                                        ]
                                    )):
        moderators_records = await self.bot.db.fetch('SELECT * FROM ubl_moderators;')
        converted_records = [list(ids) for ids in moderators_records]
        ids_list = [ids for modlist in converted_records for ids in modlist]

        embed = Embed(title='UBL Moderators Control',
                      color=0xb49dd4)

        if option == '0':
            found = False
            for ids in ids_list:
                if ids == member.id:
                    found = True
                    embed.description = f'{member.display_name} already in moderator list'
                    await inter.response.send_message(embed=embed)

            if not found:
                await self.bot.db.execute('INSERT INTO ubl_moderators VALUES ($1)', member.id)
                embed.description = f'{member.display_name} added in moderator list'
                await inter.response.send_message(embed=embed)

        elif option == '1':
            found = False
            for ids in ids_list:
                if ids == member.id:
                    found = True
                    await self.bot.db.execute('DELETE FROM ubl_moderators WHERE user_id = ($1)', (member.id))
                    embed.description = f'{member.display_name} removed from moderator list'
                    await inter.response.send_message(embed=embed)

            if not found:
                embed.description = f'{member.display_name} is not in moderator list'
                await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(UBLModeratorControl(bot))
