import discord
from discord.ext import commands


class Show_Money(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 지갑(self, ctx):

        users_money_text = open("./file/money.txt", "r", encoding='utf-8').readline()
        users_money = users_money_text.split(",")

        user_info = [0, 0]
        index = 0

        for user_money in users_money:
            if str(ctx.author.id) in user_money:
                user_info = [user_money.split(' ')[0], user_money.split(' ')[1]]
                break
            index += 1


        if int(user_info[0]) <= 0:
            embed = discord.Embed(title="[ 아직 정보가 없으셔요! ]", description='처음시작하는 유저라면, 돈받기로 돈을 받아주세요!', color=0x62c1cc)
            await ctx.send(embed=embed)
        else:
            user = await self.client.fetch_user(int(user_info[0]))
            embed = discord.Embed(title=f"[ {user.name}님의 지갑 ]", description=f'**총 E-Coin: {user_info[1]}**', color=0x62c1cc)
            embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Show_Money(client))