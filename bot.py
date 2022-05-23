import discord
from discord.ext import commands
from config import settings
import asyncio
import os
import time
settings = {
    'token': 'OTc4MjgxNTczMTc2NzA5MTkx.GY2dnU.l-bP6NKwdt8po5pKZyNPkpuPrln9yrqjwPeUUw',
    'bot': 'GuardBot',
    'id': 978281573176709191,
    'prefix': 'spam!'
}

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))



intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = settings['prefix'],  intents = intents)
client = commands.Bot(command_prefix = settings['prefix'],  intents = intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Хороший бот"))
    print("Это самолёт, а не это вертолёт")

@bot.command()
async def idiot(ctx):
    embed = discord.Embed(
    title = "Помощь по спаму",
    description = "`spam!spam_member`",
    color = ''
    )


@bot.command()
async def spam_member(ctx, member):
    for line2 in range(0 , 10000):
        channel = client.get_user(int(member))
        await channel.send('Вы были заспамлены by hlebushek! Слава Украине! Смерть России\nВы были заспамлены by hlebushek! Слава Украине! Смерть России\nВы были заспамлены by hlebushek! Слава Украине! Смерть России\nВы были заспамлены by hlebushek! Слава Украине! Смерть России\nВы были заспамлены by hlebushek! Слава Украине! Смерть России\nВы были заспамлены by hlebushek! Слава Украине! Смерть России\nВы были заспамлены by hlebushek! Слава Украине! Смерть России\nВы были заспамлены by hlebushek! Слава Украине! Смерть России\nВы были заспамлены by hlebushek! Слава Украине! Смерть России\nВы были заспамлены by hlebushek! Слава Украине! Смерть России\n')
@bot.command()
async def stop(ctx):
    await bot.change_presence(status=discord.Status.offline)
    raise SystemExit
bot.run(settings['token'])