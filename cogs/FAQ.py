import discord
from discord.ext import commands
from discord import app_commands
import random
from random import choice
import typing
Literal = typing.Literal
class FAQ(commands.Cog):

  def __init__(self, client):
        self.client = client

#  @commands.command()
#  @commands.cooldown(2, 30, commands.BucketType.user)
  @app_commands.command(name='about', description='About the RampRage project')
  @app_commands.describe(hide = "Hide the output?")
  async def about(self, interaction: discord.Interaction, hide: Literal['Yes', 'No']):
    embed = discord.Embed(title='About the project', description = f'Check out <#1010733249384960100>\nThe pin in that channel is the first message. I highly recommend you read it.', color=0x001aff)
    embed.set_footer(text = f'By the way, if you have any suggestions for the bot, let me know! Requested by {interaction.user.name}.')
    if hide == 'Yes':
      hide = True
    else:
      hide = False
    await interaction.response.send_message(embed=embed, ephemeral = hide)

#  @commands.command()
  @app_commands.command(name='changelog', description='Changelog for the latest version of the game.')
  @app_commands.describe(hide = "Hide the output?")
  async def changelog(self, interaction: discord.Interaction, hide: Literal['Yes', 'No']):
    embed = discord.Embed(title= 'Download the game', description = f"**Version 17: The AI Update** \n -Damage direction arrows \n -Crosshair added \n -Plasma drone laser attack \n Plasma drone ai \n -Upgrades to AIs in drones \n -Shotgunners now fire all projectiles in the same frame \n -Optimization on projectiles makes them appear to have triple the projectiles they do \n -Explosions no longer crash game when damaging creator of explosion or actor of same team as creator \n NEW ISSUE: explosions will not damage these actors \n-Behind the scenes code nonsense \n-Kamanzie drones now can move around corners (at cost of not turning smoothly) \n-Plasma projectiles now have a texture, the ability to be parried, and no longer get stuck on surfaces, and damage the player \n -Hitscan parry (unknown issue stops it from working right now) \n-Made MP map look more interesting for testing movement \n-Running physics on ground now no longer make player slide about like a maniac (this will be re introduced to a significantly lower extent after landing from a jump)  \n **Coming soon** \n * Version 18 is releasing by the end of December.* \n-First fully modeled and textured gun \n-Fix issue where kantanna won't go away \n -Animate kantanna slash/parry \n -Super shotgun \n -Other stuff", url = 'https://drsupervillain.itch.io/ramprage', color=0x001aff)
    embed.set_footer(text = f'Requested by {interaction.user.name}. If the changelog is outdated, DM a fast audi r8#1180.')
    if hide == 'Yes':
      hide = True
    else:
      hide = False
    await interaction.response.send_message(embed = embed, ephemeral=hide)

#  @commands.command()
#  async def betacommands(self, ctx):
#    embed = discord.Embed(title = 'Beta commands', description = f"Beta commands were certain commands that were included with the bot that only worked in a specific channel in a seperate server that only <@478212283701526529> had access to (Some were accessible on this server though). These commands were either upcoming commands or commands I'm testing. None of them were final and/or may never have made it to the normal command list. \n These are now redundant due to the `dev` branch. \n**Do not ask for an invite to that server**")
#    embed.set_footer(text=f'Requested by {ctx.message.author}')
#    await ctx.message.delete()
#    await ctx.send(embed=embed)

#  @commands.command()
  @app_commands.command(name='suggestions', description='Tells you where to put suggestions')
  @app_commands.describe(hide = 'Hide the output?')
  async def suggestions(self, interaction: discord.Interaction, hide: Literal['Yes', 'No']):
    embed = discord.Embed(title = 'Suggesting commands/features for the bot', description = f"As the bot developer has quite literally zero ideas for commands to add, he'd appreciate any suggestions you send to him! \nJust DM <@478212283701526529>.")
    embed.set_footer(text=f'Requested by {interaction.user.name}. Meme/troll suggestions will be ignored.')
    if hide == 'Yes':
      hide =  True
    else:
      hide = False
    await interaction.response.send_message(embed = embed, ephemeral=hide)

#  @commands.command()
#  async def outages(self, ctx):
#    embed = discord.Embed(title='Bot outages', description = f"~~The bot may be having some frequent outages because the site used to host the bot shares IPs with multiple people meaning that cloudfare blocks the bot from connecting to Discord becasue of how many people are using the API on the same IP.\n \nIf the bot goes offline, please ping or DM <@478212283701526529>~~ \nThis should no longer be an issue due to me migrating the bot to a new host. Outages will now mostly happen because of the server rebooting for whatever reason and the bot not starting on restart. Please DM or ping <@478212283701526529> in the event that it does go down.")
#    embed.set_footer(text = f'Requested by {ctx.message.author}')
#    await ctx.message.delete()
#    await ctx.send(embed = embed)

#  @commands.command()
  @app_commands.command(name='github', description='Shares the GitHub repo.')
  @app_commands.describe(hide = 'Hide the output?')
  async def github(self, interaction: discord.Interaction, hide: Literal['Yes', 'No']):
    embed = discord.Embed(title = 'GitHub Repository', description = f'Ever since 9/12/2022 this bot has been open sourced on GitHub. Feel free to make a pull request on the dev branch!', url = 'https://github.com/afastaudir8/discord-bot')
    embed.set_footer(text = f"Requested by {interaction.user.name}. Current bot version: 2.0.0.")
    if hide == 'Yes':
      hide = True
    else:
      hide = False
    await interaction.response.send_message(embed = embed, ephemeral=hide)

  @app_commands.command(name = 'slashcommands')
  @app_commands.describe(hide = 'Hide the output?')
  async def slashcommands(self, interaction: discord.Interaction, hide: Literal ['Yes', 'No']):
    embed = discord.Embed(title = "Slash commands", description='Since 11/12/22, the bot has migrated to using exclusively slash commands.')
    embed.set_footer(text = f'Reuqested by {interaction.user.name}')
    if hide == 'Yes':
      hide = True
    else:
      hide = False
    await interaction.response.send_message(embed = embed, ephemeral=hide)


async def setup(client):
  await client.add_cog(FAQ(client))
