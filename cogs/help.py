import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 도움(self, ctx):
        developer = await self.client.fetch_user(777496131177414656)
        bot = await self.client.fetch_user(882995163427913738)
        if ctx.author.id == 777496131177414656:
            embed = discord.Embed(title="도움말", description="E.Na봇 명령어입니다!\n봇 관리자 감지 완료!\n이 도움말은 봇 관리자 명령어가 포함되어있습니다", color=0x62c1cc)
            embed.add_field(name='**도움**', value='명령어 목록을 보여줍니다.', inline=False)
            embed.add_field(name='\n**일반**', value='`정보`, `핑`, `초대링크`, `영화랭킹`', inline=False)
            embed.add_field(name='\n**도박**', value='`도박`, `올인`, `지갑`, `돈줘`', inline=False)
            embed.add_field(name='\n**대화**', value=f'`이나야 ~`', inline=False)
            embed.add_field(name='\n\n**봇 요청, 건의**', value=f'`요청` (내용), `전송` (내용)', inline=False)
            embed.add_field(name='\n**[ 봇 관리자 명령어 ] **', value=f'```(이 아래 명령어부터는 봇 관리자만 사용가능합니다)```', inline=False)
            embed.add_field(name='\n도박 관리', value=f'`돈수정` (user_id) (돈)', inline=False)
            embed.add_field(name='\n차단 관리', value=f'`차단` [(user_id)/리스트/해제 (user_id)]', inline=False)
            embed.add_field(name='\n관리자 답장', value=f'`전송` (user_id) (내용)', inline=False)

            embed.set_thumbnail(url=bot.avatar_url)
            embed.set_footer(text=f'made by {developer}', icon_url=developer.avatar_url)

        else:
            embed = discord.Embed(title="도움말", description="E.Na봇 명령어입니다! '~'를 붙여 사용해주세요!", color=0x62c1cc)
            embed.add_field(name='**도움**', value='명령어 목록을 보여줍니다.', inline=False)
            embed.add_field(name='\n**일반**', value='`정보`, `핑`, `초대링크`, `영화랭킹`', inline=False)
            embed.add_field(name='\n**도박**', value='`도박`, `올인`, `지갑`, `돈줘`', inline=False)
            embed.add_field(name='\n**대화**', value=f'`이나야 ~`', inline=False)
            embed.add_field(name='\n**봇 요청, 건의**', value=f'`요청` (내용) / `전송` (내용)', inline=False)
            embed.set_thumbnail(url=bot.avatar_url)
            embed.set_footer(text=f'made by {developer}', icon_url=developer.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
