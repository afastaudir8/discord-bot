import discord
from discord.ext import commands

class Useful(commands.Cog):


  def __init__(self, client):
    self.client = client




  @commands.command(brief = 'Displays member count')
  async def members(self, ctx):
    membercount = ctx.guild.member_count
    embed = discord.Embed(title = 'Current Member count', description = membercount, colour=0x00FF5E)
    embed.set_footer(text=f'Requested by {ctx.message.author}.')
    await ctx.message.delete()
    await ctx.send(embed=embed)

  @commands.command(brief = 'Shows informatiion about the bot')
  async def dev(self, ctx):
    embed = discord.Embed(title = 'Bot developer', description = f'Bot created by <@478212283701526529> using the discord.py library.')
    await ctx.send(embed=embed)
  @commands.command()
  async def suicidehotlines(self, ctx):
    embed = discord.Embed(title='Suicide Prevention Hotlines', description=f"You're not alone  \n We all care about you, please **do not** go through with it. \nCall one of the crisis hotlines listed in the Wikipedia article linked in the title depending on where you are. You could also ping Ash (<@708094727588937799>) for help.", url='https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines', color=0xff0000)
    embed.set_footer(text=f'Requested by {ctx.message.author}')
    await ctx.message.delete()
    await ctx.send(embed=embed)


async def setup(client):
  await client.add_cog(Useful(client))