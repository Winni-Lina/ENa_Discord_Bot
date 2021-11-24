from random import randint

import discord
from discord.ext import commands


class Receive_Money(commands.Cog):
    def __init__(self, client):
        self.client = client





    #cogs
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
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
            user_info[1] = str(int(user_info[1])+money)
            users_money[index] = f"{user_info[0]} {user_info[1]}"
            save = open("./file/money.txt", "w", encoding="utf-8")

            if len(users_money) > 1:
                save.write(",".join(users_money))
            save.close()
            embed = discord.Embed(title=f"[ {money} E-Coin을 획득하셨습니다! ]", description=f'**총 E-Coin: {user_info[1]}**',color=0x62c1cc)
            embed.set_footer(text='1분마다 받으실 수 있습니다. 반응이 없다면 1분이 안된거에요!')
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