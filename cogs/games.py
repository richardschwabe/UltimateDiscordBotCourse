import random
from discord.ext import commands

from rps.model import RPS
from rps.parser import RockPaperScissorParser
from rps.controller import RPSGame

from hangman.controller import HangmanGame

hangman_games = {}

word = "discord"

user_guesses = list()


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

    @commands.command()
    @commands.dm_only()
    async def hm(self, ctx, guess: str):
        player_id = ctx.author.id
        hangman_instance = HangmanGame()
        game_over, won = hangman_instance.run(player_id, guess)

        if game_over:
            game_over_message = "You did not win"
            if won:
                game_over_message = "Congrats you won!!"

            game_over_message = game_over_message + \
                " The word was %s" % hangman_instance.get_secret_word()

            await hangman_instance.reset(player_id)
            await ctx.send(game_over_message)

        else:
            await ctx.send("Progress: %s" % hangman_instance.get_progress_string())
            await ctx.send("Guess so far: %s" % hangman_instance.get_guess_string())


def setup(bot):
    bot.add_cog(Games(bot))
