import os
import discord
import dotenv
from discord.ext import commands

dotenv.load_dotenv()
CTX = commands.Context

bot = commands.Bot(command_prefix='!')


@bot.command()
async def ping(ctx: CTX):
    await ctx.send('pong')
    return

@bot.command()
async def adam(ctx: CTX):
    await ctx.message.delete()
    await ctx.send('<@600944086110830593> 閉嘴!')
    return

@bot.command()
async def shutup(ctx: CTX, target: discord.Member):
    await ctx.message.delete()
    try:
        await ctx.send(f'{target.mention} 閉嘴!')
    except Exception:
        pass
    return

@bot.listen()
async def on_ready():
    print('Bot is ready')
    return
    
bot.run(os.getenv('TOKEN'))
