import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')

# Discord Conf
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", False)

DISCORD_WEBHOOK_LOTTERY_ID= os.getenv("DISCORD_WEBHOOK_LOTTERY_ID", False)
DISCORD_WEBHOOK_LOTTERY_TOKEN= os.getenv("DISCORD_WEBHOOK_LOTTERY_TOKEN", False)

# Reddit Configuration
REDDIT_APP_ID = os.getenv("REDDIT_APP_ID", False)
REDDIT_APP_SECRET = os.getenv("REDDIT_APP_SECRET", False)
REDDIT_ENABLED_MEME_SUBREDDITS = [
    'funny',
    'memes',
]
REDDIT_ENABLED_NSFW_SUBREDDITS = [
    'wtf'
]


# Permissions

MODERATOR_ROLE_NAME = "Moderator"
