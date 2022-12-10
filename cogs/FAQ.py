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
    embed = discord.Embed(title= 'Download the game', description = f"**Version 17** \n -damage direction arrows \n crosshair \n plasma drone laser attack \n plasma drone ai \n upgrades to artificial intelegence in drones \n shotgunners now fire all projectiles in the same frame \n optimization on projectiles makes them appear to have triple the projectiles they do \n explosions no longer crash game when damaging creator of explosion or actor of same team as creator \nbehind the scenes code nonsense \nkamanzie drones now can move around corners (at cost of not turning smoothly) \nplasma projectiles now have a texture,the ability to be parried,and no longer get stuck on surfaces,and damage the player \n hitscan parry (unknown issue stops it from working right now) \nmade mp map look more interestinger for testing movement \nrunning physics on ground now no longer make player slide about like a maniac (this will be re introduced to a significantly lower extent after landing from a jump) \n NEW ISSUE: explosions will not damage these actors", url = 'https://drsupervillain.itch.io/ramprage', color=0x001aff)
    embed.set_footer(text = f'Requested by {ctx.message.author}. If the changelog is outdated, DM a fast audi r8#1180. Version 18 is releasing by the end of December.')
    await ctx.message.delete()
    await ctx.send(embed = embed)

  @commands.command()
  async def betacommands(self, ctx):
    embed = discord.Embed(title = 'Beta commands', description = f"Beta commands were certain commands that were included with the bot that only worked in a specific channel in a seperate server that only <@478212283701526529> had access to (Some were accessible on this server though). These commands were either upcoming commands or commands I'm testing. None of them were final and/or may never have made it to the normal command list. \n These are now redundant due to the `dev` branch. \n**Do not ask for an invite to that server**")
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
    embed = discord.Embed(title = 'GitHub Repository', description = f'Ever since 9/12/2022 this bot has been open sourced on GitHub. Feel free to make a pull request on the dev branch!', url = 'https://github.com/afastaudir8/discord-bot')
    embed.set_footer(text = f"Requested by {ctx.message.author}. Current bot version: 1.1.1.")
    await ctx.message.delete()
    await ctx.send(embed = embed)


async def setup(client):
  await client.add_cog(FAQ(client))
