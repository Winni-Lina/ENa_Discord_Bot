import discord
from discord.ext import commands


class Block(commands.Cog):
    def __init__(self, client):
        self.client = client
        ignoreUser = open("./file/ignoreUser.txt", "r", encoding='utf-8').readline()
        self.ignore_ids = ignoreUser.split(",")

    # cogs
    @commands.command()
    async def 차단(self, ctx, *, text):
        if ctx.author.id == 777496131177414656:
            text_list = text.split(" ")
            try:
                if text_list[0] == "리스트":
                    if len(self.ignore_ids) > 1:
                        block_users_text = ""
                        for index, user in enumerate(self.ignore_ids[1:]):
                            block_users_text += f"**{index+1}.** `{await self.client.fetch_user(int(user))}` (`{user}`)\n"

                            embed = discord.Embed(title="[ 차단 리스트 ]", description=f"차단된 인원 총: {len(self.ignore_ids)-1}",
                                                  color=0x62c1cc)
                            embed.add_field(name="번호. 닉네임 (id)", value=block_users_text)
                            await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title="[ 차단된 유저가 없습니다 ]", description=f"차단된 인원 총: {len(self.ignore_ids)-1}",
                                              color=0x62c1cc)
                        await ctx.send(embed=embed)
                elif text_list[0] == "해제":
                    unblock_id = text_list[1]
                    if unblock_id in self.ignore_ids:
                        self.ignore_ids.remove(unblock_id)
                        edit_ignoreUser = open("./file/ignoreUser.txt", "w", encoding='utf-8')
                        edit_ignoreUser.write(",".join(self.ignore_ids))
                        edit_ignoreUser.close()
                        embed = discord.Embed(title="[ 해당 유저가 차단 해제 되었습니다 ]",
                                              description=f"차단 유저 닉네임(id): {await self.client.fetch_user(int(unblock_id))} ({unblock_id})",
                                              color=0x62c1cc)
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title="[ 해당 유저는 차단되어있지 않습니다 ]",
                                              description=f"차단 해제 유저 닉네임(id): {await self.client.fetch_user(int(unblock_id))} ({unblock_id})",
                                              color=0x62c1cc)
                        await ctx.send(embed=embed)
                elif int(text_list[0]):
                    if text_list[0] in self.ignore_ids:
                        embed = discord.Embed(title="[ 해당 유저는 이미 차단 되어 있습니다 ]",
                                              description=f"차단 유저 닉네임(id): {await self.client.fetch_user(int(text_list[0]))} ({text_list[0]})",
                                              color=0x62c1cc)
                        await ctx.send(embed=embed)
                    else:
                        try:
                            block_user = await self.client.fetch_user(int(text_list[0]))
                        except Exception:  # 디스코드 에러(유저를 찾을 수 없음 예외처리방법 필요)
                            embed = discord.Embed(title="[ 유저 id를 다시 확인해주세요]",
                                                  description=f"잘못된 유저 id: {text_list[0]}",
                                                  color=0x62c1cc)
                            await ctx.send(embed=embed)
                            return
                        add_ignoreUser = open("./file/ignoreUser.txt", "a", encoding='utf-8')
                        add_ignoreUser.write(f",{text_list[0]}")
                        add_ignoreUser.close()

                        embed = discord.Embed(title="[ 해당 유저가 차단 되었습니다 ]",
                                              description=f"차단 유저 닉네임(id): {block_user} ({text_list[0]})",
                                              color=0x62c1cc)
                        await ctx.send(embed=embed)
            except ValueError:
                embed = discord.Embed(title="[ 유저 id를 다시 확인해주세요 ]",
                                      description=f"잘못된 유저 id: {text_list[0]}",
                                      color=0x62c1cc)
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Block(client))
