import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 도움(self, ctx):
        await ctx.trigger_typing()

        embed = discord.Embed(title="도움말", description="이 봇은 아직 미완성인 E.Na봇입니다.", color=0x62c1cc)
        embed.add_field(name='**도움**', value='명령어 목록을 보여줍니다.', inline=False)
        embed.add_field(name='**명령어**', value='`핑`, `초대링크`, `영화랭킹`')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/843370400225820672/844955931531935804/ReactNative-snapshot-image4472701035798000406.jpg')
        embed.set_footer(text='made by 루크#8209, Jin。#5499', icon_url='https://cdn.discordapp.com/attachments/843370400225820672/844955931531935804/ReactNative-snapshot-image4472701035798000406.jpg')
        embed.add_field(name='명령어 추가 요청', value='명령어 형태로 제작할 예정입니다.', inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
