from discord.ext import commands


class Check(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 체크(self, ctx):
        await ctx.send(f"현재 총 {len(self.client.guilds)}개의 서버에 있어요!")
        print(self.client)


def setup(client):
    client.add_cog(Check(client))