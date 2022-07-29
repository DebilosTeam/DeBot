from disnake.ext import commands
from disnake import Embed

from random import choice
from datetime import datetime


class EightBall(commands.Cog):
    def __init__(self, bot):
        """Its cog for command 8ball and can't be used in another cogs or main.py"""
        self.bot = bot

    @commands.slash_command(name='8ball', description='Just a magic 8 ball')
    async def _eight_ball(self, inter, *, question):
        ball_dict = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on "
                                                                                                     "it.",
                     "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, "
                                                                                                          "try "
                                                                                                          "again.",
                     "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask "
                                                                                            "again.", "Don't count on"
                                                                                                      " it.",
                     "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        answer = choice(ball_dict)
        embed = Embed(
            title='8 Ball',
            color=0xb49dd4,
            timestamp=datetime.utcnow()
        )
        embed.add_field(name='Your question', value=f'{question}')
        embed.add_field(name='Answer', value=f'{answer}')
        await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(EightBall(bot))
