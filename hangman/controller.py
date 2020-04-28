import random

from .model import Hangman

games = {}


class HangmanGame:
    current_game = None

    def get_secret_word(self):
        return self.current_game.word

    def get_guess_string(self):
        return ",".join(self.current_game.guesses)

    def get_progress_string(self):
        return self.current_game.progress_word

    def run(self, player_id, guess):
        self.get_game(player_id)
        is_game_over, won = self.play_round(guess)
        self.save(player_id)
        return is_game_over, won

    def play_round(self, guess):
        is_word = False
        if len(guess) == 1:
            pass
        elif len(guess) > 1:
            is_word = True
        else:
            return None, None

        if not is_word:
            self.current_game.guess(guess)

        is_game_over, won = self.current_game.is_game_over(guess)
        return is_game_over, won

    def get_game(self, player_id):
        if player_id in games.keys():
            self.current_game = games[player_id]
            if self.current_game is None:
                self.create_game(player_id)
        else:
            self.create_game(player_id)

    def get_random_word(self):
        return random.choice(('discord', 'bot', 'ultimate', 'python', 'development'))

    def create_game(self, player_id):
        self.current_game = Hangman(self.get_random_word())
        self.save(player_id)

    def save(self, player_id):
        games[player_id] = self.current_game

    async def reset(self, player_id):
        games.pop(player_id)
