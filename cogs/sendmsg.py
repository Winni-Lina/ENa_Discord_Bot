import discord
from discord.ext import commands
from discord import DMChannel
import time

class sendmsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 전송(self, ctx, *, text):
        now = time.localtime()
        if ctx.author.id == 777496131177414656:
            textlist = text.split(" ")
            text = " ".join(textlist[1:])
            embed = discord.Embed(title="[ 메세지가 도착했습니다 ]", description=f"```{text}```", color=0x62c1cc)
            embed.set_author(url=ctx.author.avatar_url, name='E.Na Developer: BLUE#7608')
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.add_field(name="**답장하기**", value="~`전송` (내용)")
            embed.set_footer(text="%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
            user = await self.client.fetch_user(int(textlist[0]))
            await DMChannel.send(user, embed=embed)
        else:
            mygu = self.client.get_guild(790535644883320842)
            botch = mygu.get_channel(892019559807209473)

            embed = discord.Embed(title="[ 메세지가 도착했습니다 ]", description=f"```{text}```", color=0x62c1cc)
            embed.set_author(name=f"{ctx.author.name}")
            embed.add_field(name="유저 id", value=ctx.author.id)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text="%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

            await botch.send(embed=embed)


def setup(client):
    client.add_cog(sendmsg(client))