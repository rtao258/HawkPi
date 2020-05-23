import discord
import logging
from discord.ext import commands

# other
import cogs.aops
import cogs.amc
import playing

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(
    'hp ',
    status=discord.Status.online,
    activity=playing.activity
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

    # get token and launch bot
    with open('token.txt', 'r') as file:
        token = file.read()
        bot.run(token)
