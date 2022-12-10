import discord
from discord.ext import commands
import random
from random import choice

class FAQ(commands.Cog):

  def __init__(self, client):
        self.client = client

  @commands.command()
#  @commands.cooldown(2, 30, commands.BucketType.user)
  async def about(self, ctx):
    embed = discord.Embed(title='About the project', description = f'Check out <#1010733249384960100>\nThe pin in that channel is the first message. I highly recommend you read it.', color=0x001aff)
    embed.set_footer(text = f'By the way, if you have any suggestions for the bot, let me know! Requested by {ctx.message.author}.')
    await ctx.message.delete()
    await ctx.send(embed=embed)

  @commands.command()
  async def changelog(self, ctx):
    embed = discord.Embed(title= 'Download the game', description = f"***Version 15 Anniversary Update Changelog:***\n-AI rebuilt from the ground up. New features include:\n--4 new AI types, now with behavior patterns \n--AI now way faster and smarter\n--AI is more optimized \n--AIs now have spawnpoints \n-Added kill to heal and armor shards \n-Better hand animations\n-Fixed several dozen glitches \n-Lower filesize \n-Optimization \n-Explosions now work \n-Drones have models now \n-Fixed crashes \n-Damage works better \n***Version 15.1 Mini Update:*** \n-Sliding friction increased to 0.3 \n-Sliding in the air has no friction for smoother movement", url = 'https://drsupervillain.itch.io/ramprage', color=0x001aff)
    embed.set_footer(text = f'Requested by {ctx.message.author}. If the changelog is outdated, DM a fast audi r8#1180')
    await ctx.message.delete()
    await ctx.send(embed = embed)

  @commands.command()
  async def betacommands(self, ctx):
    embed = discord.Embed(title = 'Beta commands', description = f"Beta commands are certain commands that are included with the bot that only work in a specific channel in a seperate server that only <@478212283701526529> has access to (Some are accessible on this server though). These commands are either upcoming commands or commands I'm testing. None of them are final and/or may never make it to the normal command list \n**Do not ask for an invite to that server**")
    embed.set_footer(text=f'Requested by {ctx.message.author}')
    await ctx.message.delete()
    await ctx.send(embed=embed)

  @commands.command()
  async def suggestions(self, ctx):
    embed = discord.Embed(title = 'Suggesting commands/features for the bot', description = f"As the bot developer has quite literally zero ideas for commands to add, he'd appreciate any suggestions you send to him! \nJust DM <@478212283701526529>.")
    embed.set_footer(text=f'Requested by {ctx.message.author}. Meme/troll suggestions will be ignored.')
    await ctx.message.delete()
    await ctx.send(embed = embed)

  @commands.command()
  async def outages(self, ctx):
    embed = discord.Embed(title='Bot outages', description = f"~~The bot may be having some frequent outages because the site used to host the bot shares IPs with multiple people meaning that cloudfare blocks the bot from connecting to Discord becasue of how many people are using the API on the same IP.\n \nIf the bot goes offline, please ping or DM <@478212283701526529>~~ \nThis should no longer be an issue due to me migrating the bot to a new host. Outages will now mostly happen because of the server rebooting for whatever reason and the bot not starting on restart. Please DM or ping <@478212283701526529> in the event that it does go down.")
    embed.set_footer(text = f'Requested by {ctx.message.author}')
    await ctx.message.delete()
    await ctx.send(embed = embed)

  @commands.command()
  async def github(self, ctx):
    embed = discord.Embed(title = 'GitHub Repository', description = f'Ever since the 9th of December, 2022, this bot has been open sourced on GitHub. Feel free to make a pull request!', url = 'https://github.com/afastaudir8/discord-bot')
    embed.set_footer(text = f"Requested by {ctx.message.author}.")
    await ctx.message.delete()
    await ctx.send(embed = embed)
    
  @commands.command(brief="If you're seeing this command, the bot is currently running under another Discord bot!")
  async def botception(self, ctx):
    embed = discord.Embed(title = 'Botception', description = f'If you triggered this command, the bot is currently running under another Discord bot called dlinux! \n Basically, dlinux is a bot that creates a Linux container that is accessible via SSH that you can freely mess around with.')
    embed.set_footer(text = f'Requested by {ctx.message.author}.')
    await ctx.message.delete()
    await ctx.send(embed = embed)


async def setup(client):
  await client.add_cog(FAQ(client))
