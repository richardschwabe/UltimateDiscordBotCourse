# :bangbang: Attention :bangbang:

This code is the result of our Youtube ULTIMATE DISCORD BOT course and should not be used in production like this. The code is purely for training purposes.

# How to use this code

This code can be used alongside the ULTIMATE DISCORD BOT course.

[The playlist](https://www.youtube.com/playlist?list=PLESMQx4LeD3NmTZ8D1qwQwwSp67kznl-K) can be found here:

If you wonder what we cover and what you can find in this code have a look at the [Course Introduction](https://www.youtube.com/watch?v=yoc1XQm30SA&list=PLESMQx4LeD3NmTZ8D1qwQwwSp67kznl-K&index=2&t=0s)

If you like the content please consider subscribing to [StartupTechTutorials on Youtube](https://www.youtube.com/channel/UCIJe3dIHGq1lIAxCCwx8eyA/)

# About the structure

This Discord Bot uses [Discordpy](https://github.com/Rapptz/discord.py) and its command extension. All discord commands are structured in Cogs.

# Commands and Cogs

## Admin

- Status
- Load Cog
- Unload Cog
- Reload Cog

## Moderation

- Kick
- Ban
- Unban

## Games

- Rock Paper Scissors
- Hangman Single Player DM game
- Guess a word Multiplayer Temporary Text Channel game
- Lottery Database based multiplayer game with schedule

## Images

- Cat
- Dog
- Fox
- Random

## NSFW

- Insult

## Gamble

- Coin
- Roll
- Dice

## Basic

- owo
- invite
- poke

# Local Development Instructions

To start and deploy the bot locally the following steps are required:

```
pip install -r requirements.txt
```

Then create the following files:

```
.env
.env.debug
```

The `.env.debug` file is only parsed when you set an environment variable `DEBUG`. If it is not present it will revert to `.env`

Contents required for the `.env` or `.env.debug` file:

```
DISCORD_BOT_TOKEN=YOUR_SUBER_SECRET_DISCORD_TOKEN
```

If you want to make use of the reddit commands you also need to register an App/Bot on reddit.com and add the following lines to the .env files:

```
REDDIT_APP_ID=YOU_APP_ID
REDDIT_APP_SECRET=SUPER_SECRET_REDDIT_APP_SECRET
```

If you want to use nodemon to automatically restart the bot while developing create a nodemon config as well:

```
# ./nodemon.json:
{
  "env": {
    "DEBUG": "true"
  }
}

```

otherwise you can call the bot via:

```
export DEBUG=True python main.py
```

**_Note: export is required when you want to create the environment variable for the current shell AND all processes started from the current shell!_**

# Note

- The code is always up to date with the latest episode on the Youtube Channel
- No PR
- There will be more to come, once the tutorial series has finished!! So do come back and stay up to date

```

```
