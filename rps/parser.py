from .model import RPS


class RockPaperScissorParser:

    def __init__(self, choice):
        choice = choice.lower()

        if choice == RPS.ROCK:
            self.choice = RPS.ROCK
        elif choice == RPS.PAPER:
            self.choice = RPS.PAPER
        elif choice == RPS.SCISSOR:
            self.choice = RPS.SCISSOR
        else:
            raise
