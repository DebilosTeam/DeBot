from disnake import Intents, Game, Guild
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
        self.DEFAULT_LANG = 'en'
        self.GUILD = Guild

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
        await bot.db.execute('CREATE TABLE IF NOT EXISTS guild_configuration (id bigint, prefix text, language text);')


bot = DNUSBL()
bot.load_all_extensions()
bot.run('OTc2NTUxNzc5MTAzODM0MTY0.GMi7F7.bCvJQWwzgVF-NEmcfMw1Y2ZdsiBOVT3VT2vI9g')
