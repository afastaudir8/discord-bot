import discord
from discord.ext import commands
from discord import app_commands

class Useful(commands.Cog):


  def __init__(self, client):
    self.client = client




#  @commands.command(brief = 'Displays member count.')
  @app_commands.command(name='members', description='Displays the current member count')
  async def members(self, interaction: discord.Interaction):
    membercount = interaction.guild.member_count
    membercount = int(membercount)
#    nobotcount = membercount - 5 
    embed = discord.Embed(title = 'Current Member count', description = f"The server currently has `{membercount} members!`", colour=0x00FF5E)
    embed.set_footer(text=f'Requested by {interaction.user.name}.')
    await interaction.response.send_message(embed=embed)

#  @commands.command(brief = 'Shows credits for the bot.')
  @app_commands.command(name='credits', description='Shows credits for the bot.')
  async def credits(self, interaction: discord.Interaction):
    embed = discord.Embed(title = 'Credits', description = f'Bot created by <@478212283701526529> using the discord.py library. Other libraries include Translator, goslate, datetime, and asyncio \n Check out the source code here: https://github.com/afastaudir8/discord-bot', url='https://github.com/afastaudir8/discord-bot', colour=0x00FFF3)
    embed.set_footer(text=f"Requested by {interaction.user.name}. Current bot version: 2.0.0.")
    await interaction.response.send_message(embed=embed)

#  @commands.command()
  @app_commands.command(name='suicidehotlines', description='Displays a Wikipedia page for suicide hotlines.')
  async def suicidehotlines(self, ctx):
    embed = discord.Embed(title='Suicide Prevention Hotlines', description=f"You're not alone  \n We all care about you, please **do not** go through with it. \nCall one of the crisis hotlines listed in the Wikipedia article linked in the title depending on where you are. You could also ping Ash (<@708094727588937799>) for help.", url='https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines', color=0xff0000)
    embed.set_footer(text=f'Requested by {ctx.message.author}')
    await ctx.message.delete()
    await ctx.send(embed=embed)


async def setup(client):
  await client.add_cog(Useful(client))