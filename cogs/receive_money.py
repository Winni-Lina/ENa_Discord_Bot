from random import randint

import discord
from discord.ext import commands


class Receive_Money(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 돈줘(self, ctx):

        users_money_text = open("./file/money.txt", "r", encoding='utf-8').readline()
        users_money = users_money_text.split(",")

        user_info = [0, 0]
        index = 0

        for user_money in users_money:
            if str(ctx.author.id) in user_money:
                user_info = [user_money.split(' ')[0], user_money.split(' ')[1]]
                break
            index += 1

        money = randint(2500, 4500)

        if int(user_info[0]) > 0:
            embed = discord.Embed(title="[ 아직 기능이 완성되지 않았어요..ㅠ ]", description='개발자님께 요청을 보내시면, 돈을 드릴거에여', color=0x62c1cc)
            await ctx.send(embed=embed)
        else:
            add = open("./file/money.txt", "a", encoding="utf-8")
            add.write(f",{ctx.author.id} 1000000")
            add.close()
            embed = discord.Embed(title="[ E.NA 도박을 처음 시작하시는군요! ]", description='첫 지급으로 `100,000` E-Coin을 지급해드렸어요!', color=0x62c1cc)
            embed.set_footer(text="'~도박'을 통해 도박을 즐겨보세요!")
            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Receive_Money(client))