from disnake import Intents
from disnake.ext import commands

from json import load
from os import listdir
from asyncpg import create_pool


def get_config():
    with open(f'config.json') as config_file:
        return load(config_file)


class DeBot(commands.Bot):
    def __init__(self):
        super().__init__(
            help_command=None,
            intents=Intents.all(),
            sync_commands_debug=True,
        )

    def load_all_extensions(self):
        for command_folder in listdir(f'commands/.'):
            for command in listdir(f'commands/{command_folder}/.'):
                if command.endswith('.py'):
                    bot.load_extension(f'commands.{command_folder}.{command[:-3]}')

        for event in listdir('events/'):
            if event.endswith('.py'):
                self.load_extension(f'events.{event[:-3]}')

    async def create_db_pool(self):
        bot.db = await create_pool(dsn='postgres://postgres:1234@localhost:5432/debot')
        await bot.db.execute('CREATE TABLE IF NOT EXISTS profiles (id bigint, prefix text);')


bot = DeBot()
bot.load_all_extensions()
bot.run(get_config()['token'])
