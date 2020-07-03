# -*- coding: utf-8 -*-

from discord.ext import commands
from random import choice


class Quote(commands.Cog):
    """The description for Quote goes here."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command
    async def quote(self, ctx):
        """Get a random quote from the quote board."""
        quotes_channel = ctx.guild.get_channel(717398911949471785)
        quotes = []
        async for message in quotes_channel.history():
            quotes.append((message.content, message.author))
        quote, author = choice(quotes)
        await ctx.send(quote)
        await ctx.send(f"Contributed by {author}.")


def setup(bot):
    bot.add_cog(Quote(bot))
