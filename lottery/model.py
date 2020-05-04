import random
import datetime

from mongoengine import *


class LotteryDrawing(Document):

    TYPE_USER = "user"
    TYPE_SYSTEM = "system"

    TYPE_CHOICES = [TYPE_SYSTEM, TYPE_USER]

    numbers = ListField()

    members_id = IntField(required=False)

    dtype = StringField(choices=TYPE_CHOICES, default=TYPE_USER)

    created_at = DateTimeField()
    updated_at = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        return super(LotteryDrawing, self).save(*args, **kwargs)

    def draw_numbers(self):
        numbers = random.sample(range(1, 50), k=6)
        return sorted(numbers)

    def numbers_as_string(self):
        return ",".join(str(x) for x in self.numbers)
