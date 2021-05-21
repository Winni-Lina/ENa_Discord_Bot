import discord
from discord.ext import commands
import time

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 도움(self, ctx):
        await ctx.trigger_typing()
        embed = discord.Embed(title="아직 제작중입니다.")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))