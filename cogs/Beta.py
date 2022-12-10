import discord
from discord.ext import commands
import random
from random import choice
import goslate
import time


class Beta(commands.Cog):

  def __init__(self, client):
        self.client = client

#  @commands.command()
#  async def vergil(self, ctx):
#    channel = self.client.get_channel(738185519258927158)
#    await channel.send('https://tenor.com/view/vergil-gif-25306498')
  
#  @commands.command()
#  async def rulesofnature(self, ctx):
#    channel = self.client.get_channel(738185519258927158)
#    await channel.send('https://tenor.com/view/metal-gear-rising-metal-gear-raiden-metal-gear-ray-super-strength-gif-14889306')



  
#  @commands.command()
#  async def suicidehotlines(self, ctx):
#    embed = discord.Embed(title='Suicide Prevention Hotlines', description=f"You're not alone  \n We all care about you, please **do not** go through with it. \nCall one of the crisis hotlines listed in the Wikipedia article linked in the title depending on where you are. You could also ping Ash (<@708094727588937799>) for help.", url='https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines', color=0xff0000)
#    embed.set_footer(text=f'Requested by {ctx.message.author}.')
#    channel = self.client.get_channel(738185519258927158)
#    await ctx.messsage.delete()
#    await channel.send(embed=embed)

#  @commands.command()
#  async def translation(self, ctx, message):
#    gs = goslate.Goslate()
#    trans = gs.translate(message, 'en')
#    embed = discord.Embed (title='Translation', description = f"Translation result: {trans}")
#    embed.set_footer(text=f'Demandé par {ctx.message.author}.')
#    await ctx.send(embed=embed) 








async def setup(client):
  await client.add_cog(Beta(client))
