import discord
from discord.ext import commands
import time

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 테스트(self, ctx):
        # 명령어 내용 입력
        await ctx.send('OK')


def setup(client):
    client.add_cog(Test(client))