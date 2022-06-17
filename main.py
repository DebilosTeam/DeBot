from disnake import Intents
from disnake.ext import commands

from cogs.events.ready import get_prefix
from asyncpg import create_pool
from os import listdir


class DeBot(commands.Bot):
    def __init__(self):
        super().__init__(
            help_command=None,
            command_prefix=get_prefix,
            intents=Intents.all(),
            sync_commands_debug=True,
        )

    def load_all_extensions(self):
        for event in listdir('cogs/events'):
            if event.endswith('.py'):
                self.load_extension(f'cogs.events.{event[:-3]}')

        for command in listdir('cogs/commands'):
            if command.endswith('.py'):
                self.load_extension(f'cogs.commands.{command[:-3]}')

    async def create_db_pool(self):
        bot.db = await create_pool(dsn='postgres://postgres:1234@localhost:5432/debot')
        await bot.db.execute('CREATE TABLE IF NOT EXISTS guild_configuration (id bigint, prefix text);')


bot = DeBot()
bot.load_all_extensions()
bot.run('')
