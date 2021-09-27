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
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/891875793783902218/891875843826135040/29841_R8odfZL3.png')
        embed.set_footer(text='made by BLUE#7608', icon_url='https://cdn.discordapp.com/avatars/777496131177414656/eedb299fd8b1860a80b15a5c0c5d5168.webp?size=1024')
        embed.add_field(name='명령어 추가 요청', value='명령어 형태로 제작할 예정입니다.', inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
