from discord.ext import commands


class Check(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 체크(self, ctx):
        await ctx.send(f"I'm in {len(self.client.guilds)} servers!")
        print(self.client)


def setup(client):
    client.add_cog(Check(client))