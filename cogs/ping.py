from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 핑(self, ctx):
        await ctx.send(f'퐁! `{round(self.client.latency*1000)} ms`')


def setup(client):
    client.add_cog(Ping(client))