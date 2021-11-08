import discord
from discord.ext import commands

class InviteLink(commands.Cog):
    def __init__(self, client):
        self.client = client

    # cogs
    @commands.command()
    async def 초대링크(self, ctx):
        await ctx.trigger_typing()

        embed = discord.Embed(title='Disbot 봇을 초대할 수 있는 링크입니다', color=0x62c1cc)
        embed.add_field(name='초대링크', value='[Link](<https://discord.com/api/oauth2/authorize?client_id=882995163427913738&permissions=8&scope=bot>)')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(InviteLink(client))