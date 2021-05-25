from discord.ext import commands
import discord
import requests
from bs4 import BeautifulSoup



class MovieRank(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 영화랭킹(self, ctx):
        response = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        ranking = 1
        embed = discord.Embed(title="영화 랭킹", description="[네이버 영화 랭킹](<https://movie.naver.com/movie/sdb/rank/rmovie.nhn>)입니다", color=0x62c1cc)

        for tag in soup.select('div[class=tit3]'):
            embed.add_field(name=f"{ranking}위", value=f'[{tag.text.strip()}](<{"https://movie.naver.com" + tag.find("a")["href"]}>)')
            ranking = ranking + 1
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(MovieRank(client))

