
import schedule
import time

from lottery.controller import LotteryController

import requests
from discord import Webhook, RequestsWebhookAdapter

from settings import *


def job():
    dc = LotteryController()
    numbers = dc.draw_numbers()
    #numbers_str = ",".join(str(x) for x in numbers)
    numbers_str = "3,5,12,15,29,17"
    webhook = Webhook.partial(DISCORD_WEBHOOK_LOTTERY_ID,
                              DISCORD_WEBHOOK_LOTTERY_TOKEN, adapter=RequestsWebhookAdapter())
    webhook.send(numbers_str, username="Webhook Guy")


schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
