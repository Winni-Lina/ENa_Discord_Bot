import discord
from discord.ext import commands

<<<<<<< HEAD
=======

>>>>>>> 71da92cd80f3d8d440c97a33662a4a10e01f4dc0
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

<<<<<<< HEAD
    #commands
    @commands.command()
    async def 도움(self, ctx):
=======
    # cogs
    @commands.command()
    async def 도움(self, ctx):
        # 명령어 내용 입력
>>>>>>> 71da92cd80f3d8d440c97a33662a4a10e01f4dc0
        await ctx.trigger_typing()
        embed = discord.Embed(title="아직 제작중입니다.")
        await ctx.send(embed=embed)


def setup(client):
<<<<<<< HEAD
    client.add_cog(Help(client))
=======
    client.add_cog(Help(client))
>>>>>>> 71da92cd80f3d8d440c97a33662a4a10e01f4dc0
