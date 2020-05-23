import discord
from discord.ext import commands
import time


class Meta(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command()
    async def stats(self, ctx):
        time_delta = time.time() - self.start_time
        result = discord.Embed(
            title="HawkPi Bot Stats",
            description=f"Up time: {round(time_delta, 3)} s\n"
                        f"Latency: {round(1000 * self.bot.latency, 3)} ms"
        )
        await ctx.send(embed=result)


def setup(bot):
    bot.add_cog(Meta(bot))
