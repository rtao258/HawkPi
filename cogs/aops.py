# discord
from discord.ext import commands
import discord
# web
import requests  # TODO: use aiohttp
from bs4 import BeautifulSoup


class AoPS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="amc")
    async def get_amc_problem(self, ctx, year, test, question):
        question = AMCQuestion(year, test, question)
        result = discord.Embed(
            title=question.get_question_name(),
            type='rich',
            description=question.get_problem_text(),
            url=question.get_url(),
        )
        result.set_image(url=question.get_answer_choices())
        message = await ctx.send(embed=result)
        # answer choices
        for choice in '🇦🇧🇨🇩🇪':
            await message.add_reaction(choice)

    @commands.command()
    async def aime(self, ctx, year, test, question):
        question = AIMEQuestion(year, test, question)
        result = discord.Embed(
            title=question.get_question_name(),
            type='rich',
            description=question.get_problem_text(),
            url=question.get_url(),
        )
        result.set_image(url=question.get_answer_choices())
        await ctx.send(embed=result)


class Question:
    """
    Question from AMC contest on AoPS wiki
    """

    contest = None

    def __init__(self, year, test, number):
        self.year = year
        self.test = test
        self.number = number
        self.soup = None
        self.soupify()

    def get_url(self):
        wiki = 'https://artofproblemsolving.com/wiki/index.php'
        return f'{wiki}/{self.year}_{type(self).contest}_{self.test}_Problems/Problem_{self.number}'

    def soupify(self):
        response = requests.get(self.get_url())
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def get_question_name(self):
        return f"{self.year} {type(self).contest} {self.test} Problem {self.number}"

    def get_problem_text(self):
        return self.soup.find(class_='mw-parser-output').find_next('p').text

    def get_answer_choices(self):
        img = self.soup.find(class_='mw-parser-output').find_next('p').next_sibling.find('img')
        return 'https:' + img['src']


class AMCQuestion(Question):
    contest = 'AMC'


class AIMEQuestion(Question):
    contest = 'AIME'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test = self.test.upper()


def setup(bot):
    bot.add_cog(AoPS(bot))
