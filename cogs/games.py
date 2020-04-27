import random
from discord.ext import commands

from rps.model import RPS
from rps.parser import RockPaperScissorParser
from rps.controller import RPSGame


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage="rock | paper | scissor")
    async def rps(self, ctx, user_choice: RockPaperScissorParser = RockPaperScissorParser(RPS.ROCK)):
        """
        Play a game of Rock Paper Scissors

        Either choose rock, paper or scissor and beat the bot

        You cannot challenge another user. Its you vs the bot only!
        """
        game_instance = RPSGame()

        user_choice = user_choice.choice

        won, bot_choice = game_instance.run("asd")

        if won is None:
            message = "It's a draw! Both chose: %s" % user_choice
        elif won is True:
            message = "You win: %s vs %s" % (user_choice, bot_choice)
        elif won is False:
            message = "You lose: %s vs %s" % (user_choice, bot_choice)

        await ctx.send(message)


def setup(bot):
    bot.add_cog(Games(bot))
