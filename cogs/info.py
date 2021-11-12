import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 정보(self, ctx):
        developer = await self.client.fetch_user(777496131177414656)
        bot = await self.client.fetch_user(882995163427913738)

        embed = discord.Embed(title='[ 봇 정보 ]', description='다기능 봇으로 발전할 E.Na 봇입니다!', color=0x62c1cc)
        embed.add_field(name='< 설명 >', value='```아직 기능이 많이 부족해요.. \n그래서 요청이나 전송 기능으로 다양한 의견을 받고 있어요!\n더욱 발전할 수 있는 E.Na봇이 될 수 있도록\n노력할게요!```', inline=False)
        embed.add_field(name='< 봇 사용 서버 수 >', value=f'서버 수: {len(self.client.guilds)}', inline=True)
        embed.add_field(name='< 개발자 >', value=developer, inline=True)
        embed.set_thumbnail(url=bot.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))