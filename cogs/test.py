import discord
from discord.ext import commands
import time

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    #commands
    @commands.command()
    async def 테스트(self, ctx):
        await ctx.send("OK")


def setup(client):
    client.add_cog(Test(client))