from disnake import ui, Embed, SelectOption, MessageInteraction
from disnake.ext import commands

from datetime import datetime


class Embeds:
    pageone = Embed(
        title='User commands',
        description='Here will be user commands',
        color=0xb49dd4,
        timestamp=datetime.utcnow()
    )
    pageone.set_footer(text='Copyright © Debilos Team 2022')

    pagetwo = Embed(
        title='Fun commands',
        description='Here will be fun commands',
        color=0xb49dd4,
        timestamp=datetime.utcnow()
    )
    pagetwo.set_footer(text='Copyright © Debilos Team 2022')

    pagethree = Embed(
        title='Server owner commands',
        description='Here will be server owner commands',
        color=0xb49dd4,
        timestamp=datetime.utcnow()
    )
    pagethree.set_footer(text='Copyright © Debilos Team 2022')


class Dropdown(ui.Select):
    def __init__(self):
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
            await interaction.response.edit_message(embed=Embeds.pageone)
        elif self.values[0] == 'Fun commands':
            await interaction.response.edit_message(embed=Embeds.pagetwo)
        elif self.values[0] == 'Server owner commands':
            await interaction.response.edit_message(embed=Embeds.pagethree)


class DropdownView(ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Dropdown())


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def help(self, ctx):
        view = DropdownView()

        helpembed = Embed(title='Commands list',
                          description='Hello, you called help command, all the bot commands will be here',
                          color=0xb49dd4,
                          timestamp=datetime.utcnow())

        helpembed.set_footer(text='Copyright © Debilos Team 2022')

        await ctx.send(embed=helpembed, view=view)


def setup(bot):
    bot.add_cog(Help(bot))
