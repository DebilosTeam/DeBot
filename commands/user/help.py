from disnake.ext import commands
from disnake import ui, Embed, SelectOption, MessageInteraction

from datetime import datetime


class Embeds:
    page_one = Embed(
        title='User commands',
        description='Here will be user commands',
        color=0xb49dd4,
        timestamp=datetime.utcnow()
    )

    page_two = Embed(
        title='Fun commands',
        description='Here will be fun commands',
        color=0xb49dd4,
        timestamp=datetime.utcnow()
    )

    page_three = Embed(
        title='Server owner commands',
        description='Here will be server owner commands',
        color=0xb49dd4,
        timestamp=datetime.utcnow()
    )


class Dropdown(ui.Select):
    def __init__(self):
        """Its init dropdown menu for help cog only"""
        options = [
            SelectOption(label='User commands', description='Commands available to all'),
            SelectOption(label='Fun commands', description='Just commands like 8ball and etc'),
            SelectOption(label='Server owner commands', description='Commands for bot control'),
        ]

        super().__init__(
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: MessageInteraction):
        if self.values[0] == 'User commands':
            await interaction.response.edit_message(embed=Embeds.page_one)
        elif self.values[0] == 'Fun commands':
            await interaction.response.edit_message(embed=Embeds.page_two)
        elif self.values[0] == 'Server owner commands':
            await interaction.response.edit_message(embed=Embeds.page_three)


class DropdownView(ui.View):
    def __init__(self):
        """Adding of dropdown menu for help embed"""
        super().__init__()

        self.add_item(Dropdown())


class Help(commands.Cog):
    def __init__(self, bot):
        """Its cog for command help and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(description='Send bot command list')
    async def help(self, inter):
        view = DropdownView()

        help_embed = Embed(title='Commands list',
                           description='Hello, you called help command, all the bot commands will be here',
                           color=0xb49dd4,
                           timestamp=datetime.utcnow())

        await inter.response.send_message(embed=help_embed, view=view)


def setup(bot):
    bot.add_cog(Help(bot))
