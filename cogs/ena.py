from discord.ext import commands


class Ena(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 이나야(self, ctx, *, text):
        text_list = text.split(" ")

        if text_list[0]:
            await ctx.send("이나도 심심해요..ㅠ")


def setup(client):
    client.add_cog(Ena(client))