import os
from multiprocessing import Event
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import os

import random
from random import choice
import asyncio

 
intents= discord.Intents.all()
intents.members=True

client = commands.Bot(command_prefix = '*', intents=intents)

token = open('token.txt', 'r')
tokenstring = token.read()

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


game = discord.Game('Ramprage')

@client.event
async def on_ready():
  await client.change_presence(activity=game)
  print('ready')
  
@client.event 
async def on_member_remove(member):
 channel=client.get_channel(1005707501435629752)
 await channel.send(f'{member} has left the server! :(')

@client.event
async def on_member_join(member):
    guild = client.get_guild(1005707501435629749)
    channel=client.get_channel(1005707501435629752)
    await channel.send(f"Hello {member.mention}! Welcome to this server! You are now the {guild.member_count}th member! \nBefore anything, I recommend you go to <#1008126343738830848> and familiarize yourself with the rules. \n<#1007345658136625203> contains the download link to the game (You can also get the link by using the changelog command). \nFinally, to learn more on the game, check out <#1010733249384960100> \nTo learn how to use this bot, use *help.")


async def main():
    async with client:
        await load_extensions()
        await client.start(tokenstring)


#keep_alive()
asyncio.run(main())
