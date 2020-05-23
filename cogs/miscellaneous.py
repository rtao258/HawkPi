import asyncio
import discord
from discord.ext import commands


class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        await ctx.send(f"Hello, @{member}!")

    @commands.command()
    async def donate(self, ctx):
        await ctx.send(f"I'm not taking donations of real money right now, "
                       f"but you can try `p!pay @21taoray 10`!")

    @commands.command()
    async def crash(self, ctx):
        raise discord.DiscordException

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Hello, I am talking.", tts=True)

    @commands.command()
    async def emojis(self, ctx):
        for emoji in ctx.guild.emojis:
            await ctx.send(f':{emoji.name}:\t{emoji.id}')

    @commands.command()
    async def spam(self, ctx, times=100, delay=2):
        for _ in range(times):
            await ctx.send("@21taoray is irresponsible! He has designed me with a feature to spam this server.")
            await asyncio.sleep(delay)


def setup(bot):
    bot.add_cog(Miscellaneous(bot))
