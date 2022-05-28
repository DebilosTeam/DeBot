from disnake import Intents, Game
from disnake.ext import commands

from os import listdir
from asyncpg import create_pool
from cogs.events.prefix_getting import get_prefix


class DNUSBL(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=get_prefix,
            intents=Intents.all(),
            sync_commands_debug=True,
            help_command=None
        )

    def load_all_extensions(self):
        for event in listdir('cogs/events'):
            if event.endswith('.py'):
                self.load_extension(f'cogs.events.{event[:-3]}')
                print(f'Event cog {event[:-3]}, Loaded!')

        for command in listdir('cogs/commands'):
            if command.endswith('.py'):
                self.load_extension(f'cogs.commands.{command[:-3]}')
                print(f'Command cog {command[:-3]} loaded!')

    async def on_ready(self):
        print(
            f"The bot is ready.\n"
            f"User: {self.user}\n"
            f"ID: {self.user.id}"
        )
        await bot.change_presence(activity=Game(name='/help'))

    async def create_db_pool(self):
        bot.db = await create_pool(dsn='postgres://postgres:1234@localhost:5432/dnusbl')


bot = DNUSBL()
bot.load_all_extensions()
bot.run('')
