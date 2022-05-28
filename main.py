from disnake import Intents, Message, Game, Guild
from disnake.ext import commands

import asyncpg
from os import listdir
from json import load, dump

DEFAULT_PREFIX = '-'

class DNUSBL(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=DEFAULT_PREFIX,
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
        db = await asyncpg.create_pool(dsn='postgres://postgres:1234@localhost:5432/dnusbl-db')
        await db.execute('CREATE TABLE IF NOT EXISTS guild_prefixes(id bigint, prefix text)')
        await db.execute('CREATE TABLE IF NOT EXISTS banlists(guild_id bigint, banned_users bigint)')


bot = DNUSBL()
bot.load_all_extensions()
bot.loop.run_until_complete(bot.create_db_pool())
bot.run('OTc2NTUxNzc5MTAzODM0MTY0.G0tJnh.7hTd-2a-fUxIdoWIEKSR8RC6EVSBji_IzDrfy8')
