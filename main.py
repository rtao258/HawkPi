import discord
from discord.ext import commands

import os
import logging
from dotenv import load_dotenv

import playing

# get token as environment variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(
    'hp ',
    status=discord.Status.online,
    activity=playing.choose_activity()
)


@bot.event
async def on_connect():
    logging.info('Connected to discord')


@bot.event
async def on_ready():
    logging.info('Logged in as {0.user}'.format(bot))


if __name__ == '__main__':
    # cogs
    cogs = [
        'cogs.meta',
        'cogs.amc',
        'cogs.aops',
        'cogs.miscellaneous'
    ]
    logging.info(f"Attempting to add {len(cogs)} cogs")
    for cog in cogs:
        bot.load_extension(cog)
        logging.info(f"Added {cog} cog")

    # launch bot
    bot.run(TOKEN)
