import discord
from discord.ext import commands

from config import *

intents = discord.Intents.default()

bot = commands.Bot(PREFIX, intents=intents)  # check config


# examples event
@bot.event
async def on_ready():
    print('bor active')


@bot.event
async def on_message(ctx: commands.context.Context):
    await ctx.send(f"your message: {ctx.message}")


# examples command
@bot.command(name='hello')
async def hello(ctx: commands.context.Context):
    await ctx.reply('Hello')

bot.run(TOKEN)  # check config
