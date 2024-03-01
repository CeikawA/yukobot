import discord
import os
from discord.ext import commands

# 봇 설정
TOKEN = 'MTIxMjMzNTkzNDA1NDYwNDg2MA.GDc-iw.0eNDLRLl9pBRP9at4_gUVjWMpEDRvPZqdENBrs'
PREFIX = '!'  # 봇의 명령 접두사를 설정합니다.

# Privileged Intent 비활성화
intents = discord.Intents.all()
intents.typing = True
intents.presences = True
intents.members = True

# 봇 객체 생성
bot = commands.Bot(command_prefix='유코야 ' , intents=intents)

# 봇이 준비되었을 때 동작할 함수
@bot.event
async def on_ready():
    print(f'{bot.user}로 로그인하였습니다.')

# "!안녕" 명령어 처리 함수
@bot.command()
async def 안녕(ctx):
    await ctx.channel.send('안녕!')

@bot.command()
async def ceikawa(ctx):
    await ctx.channel.send('CeikawA님! 내 주인님이야!')

    

access_token = os.environ["BOT_TOKEN"]
# 봇 실행
bot.run(access_token)





