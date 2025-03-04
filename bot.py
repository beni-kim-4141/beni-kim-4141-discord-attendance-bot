import discord
import asyncio
import os
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ 로그인 성공: {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("안녕! 😊")

# 자동 종료 (16시간 후)
async def shutdown():
    await asyncio.sleep(3600 * 16)  # 16시간 후 자동 종료
    exit()

asyncio.run(shutdown())

bot.run(TOKEN)
