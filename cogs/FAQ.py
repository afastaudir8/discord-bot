import discord
from discord.ext import commands
import random
from random import choice

class FAQ(commands.Cog):

  def __init__(self, client):
        self.client = client

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
    embed.set_footer(text = f"Requested by {ctx.message.author}. Current bot version: 1.2.0.")
    await ctx.message.delete()
    await ctx.send(embed = embed)


async def setup(client):
  await client.add_cog(FAQ(client))
