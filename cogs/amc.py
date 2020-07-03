import discord
from discord.ext import commands


class AMC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def score(self, ctx: commands.Context, correct, incorrect, skipped, aime=0):
        """Calculates an AMC score / USA(J)MO index."""
        correct = int(correct)
        incorrect = int(incorrect)
        skipped = int(skipped)
        amc_s, aime_s, index = score(correct, incorrect, skipped, aime)
        result = discord.Embed(
            title="AMC Scoring",
            type='rich',
            description=f"Your AMC score is {amc_s}/150.\n"
                        f"Your AIME score is {aime_s}/15.\n"
                        f"Your USA(J)MO qualification index \t {index}/300.\n"
        )
        await ctx.send(embed=result)


def score(correct, incorrect, skipped, aime=0):
    """
    calculates scores for MAA contests
    :param correct: correctly answered problems on AMC
    :param incorrect: incorrectly answered problems on AMC
    :param skipped: skipped problems on AMC
    :param aime: correctly answered problems on AIME
    :return: AMC score, AIME score, and USA(J)MO qualification index
    """
    total_problems = correct + incorrect + skipped
    if total_problems != 25:
        raise ValueError(f"Total problems don't add up to {total_problems}, not 25!")
    correct_score = 6.0 * correct
    skipped_score = 1.5 * skipped
    amc_score = correct_score + skipped_score
    aime_score = 10 * aime
    index = amc_score + aime_score
    return amc_score, aime, index


def setup(bot):
    bot.add_cog(AMC(bot))
