import os
from multiprocessing import Event
import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import has_permissions
import os
import sys
import platform
import random
from random import choice
import asyncio

system = platform.system()

if "Linux" not in (system):
    print("By the way, I haven't tested this bot on anything other than Linux. While there shouldn't be any compatiblity issues, keep that in mind.")


# This is such a god awful way of doing this kind of thing. Everything until "exitcode()" is basically just
# 1: Check if the token.txt file (the file that contains a Discord token) exists. This was purely made so I don't accidentally commit my bot token to the repo
# 2: If the file doesn't exist, write "This is where you put the bot's Discord token. Replace all the text here with just your token." to exit the script in such an awful way
# 2.5: If the file does exist, it prints the token and start the bot
# 3 Verify the contents of token.txt. If it contains "This is where you put the bot's Discord token. Replace all the text here with just your token.", exit the script.


def exitcode():
    tokencheck = open('token.txt', 'r')
    tokenread = tokencheck.read()
    if tokenread == "This is where you put the bot's Discord token. Replace all the text here with just your token.":
        print("Check out the newly created text file in the bot's directory. That's where you have to put your bot's token.")
        print('Exiting...')
        sys.exit(0)
    else:
        print(f"Your token: {tokenread}")



exitcode()

intents= discord.Intents.all()
intents.members=True

client = commands.Bot(command_prefix = '*', intents=intents)

token = open('token.txt', 'r')
tokenstring = token.read()

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


game = discord.Game("around in VSCode")

@client.event
async def on_ready():
  await client.change_presence(activity=game)
  print('ready (dev)')
  try:
    synced = await client.tree.sync()
    print(f'Synced. {len(synced)} commands.)')
  except Exception as error:
    print(error)


  
@client.event 
async def on_member_remove(member):
 channel=client.get_channel()
 await channel.send(f'{member} has left the server! :(')

@client.event
async def on_member_join(member):
    guild = client.get_guild()
    channel=client.get_channel()
    await channel.send(f"Hello {member.mention}! Welcome to this server! You are now the {guild.member_count}th member! \nBefore anything, I recommend you go to <#1008126343738830848> and familiarize yourself with the rules. \n<#1007345658136625203> contains the download link to the game (You can also get the link by using the changelog command). \nFinally, to learn more on the game, check out <#1010733249384960100> \nTo learn how to use this bot, use *help.")


async def main():
    async with client:
        await load_extensions()
        await client.start(tokenstring)


#keep_alive()
asyncio.run(main())
