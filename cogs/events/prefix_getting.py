from disnake.ext import commands

DEFAULT_PREFIX = '-'
DEFAULT_LANG = 'en'


async def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or(DEFAULT_PREFIX)(bot, message)

    prefix = await bot.db.fetch('SELECT prefix FROM guild_configuration WHERE "id" = $1', message.guild.id)
    if len(prefix) == 0:
        await bot.db.execute('INSERT INTO guild_configuration("id", prefix) VALUES ($1, $2)', message.guild.id, DEFAULT_PREFIX)
        prefix = DEFAULT_PREFIX
    else:
        prefix = prefix[0].get("prefix")
    return commands.when_mentioned_or(prefix)(bot, message)


class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Prefix(bot))
    bot.loop.run_until_complete(bot.create_db_pool())
