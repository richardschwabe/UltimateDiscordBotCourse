class GuessAWord:
    word = ""
    category = ""
    channel_id = ""
    channel_name = ""

    def __init__(self, word, category):
        self.word = word
        self.category = category

    def guess(self, word):
        if word == self.word:
            return True, ""
        else:
            if word.lower() in self.word.lower():
                return False, word
        return False, ""
