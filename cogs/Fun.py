import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
from random import choice
import goslate
import datetime
from googletrans import Translator

translation = Translator(service_urls=['translate.googleapis.com'])

Primaries = ['R-201/101', 'Hemlock', 'G2A5', "Flatline", 'Alternator', 'CAR', 'R-97', 'Volt', 'Spitfire', 'Devotion', 'L-STAR', 'Cold War', 'EPG', 'SMR', 'Softball', 'Wingman Elite', 'Mozambique', 'EVA-8', 'Mastiff', 'Double Take', 'Kraber', 'Longbow']
Secondaries = ['P2016', 'Wingman', 'RE-45']
AntiTitan = ['Charge Rifle','MGL', 'Thunderbolt', 'Archer']
Perk1 = ['Power Cell', 'Fast Regen', 'Ordanance Expert', 'Phase Embark']
Perk2 = ['Kill Report', 'Wallhang', 'Hover', 'Low Profile', 'Titan Hunter']
Ability = ['Cloak', 'Grapple', 'Pulse Blade', 'Holo Pilot', 'Stim', 'A-Wall']

def Select():
    global P
    global S
    global AT
    global P1
    global P2
    global A
    P = random.choice(Primaries)
    S = random.choice(Secondaries)
    AT= random.choice(AntiTitan)
    P1 = random.choice(Perk1)
    P2 = random.choice(Perk2)
    A = random.choice(Ability)

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command()
    @has_permissions(manage_messages=True)
    async def say(self, ctx, message=None):
        await ctx.send(message)
        await ctx.message.delete()

#    @commands.command()
#    @has_permissions(manage_messages=True)
#    async def sendembed(self, ctx, message=None):
#      embed = discord.Embed(title='Embed:', description = ctx.message)
#      embed.set_footer(f'Sent by {ctx.message.author}')
#      await ctx.send(embed=embed)

    @commands.command()
    async def gaymachine(self, ctx):
      gaymachine = random.randint(1,100)
      embed = discord.Embed(title='Gayness Percentage:', description=f'{gaymachine}%')
      await ctx.send(embed=embed)

    @commands.command(brief ='Loadout generator for Titanfall 2')
    async def tf2loadout(self, ctx):
      Select()
      embed = discord.Embed(title='Titanfall 2 Loadout Generator', description = f'**Primary:** {P}\n**Secondary:** {S}\n**Anti-Titan:** {AT}\n**Kit 1:** {P1}\n**Kit 2:** {P2}\n**Ability:** {A}', colour=0x00f6fa)
      embed.set_footer(text = f"Based off of a fast audi r8#1180's original CLI loadout generator. Requested by {ctx.message.author}")
      await ctx.message.delete()
      await ctx.send(embed = embed)
    
    @commands.command(brief = "Translates your message", description = 'This command grabs your message and puts it through the Google Translate API. Sometimes, it just decides to stop working, sorry about that!')
    async def gtranslate(self, ctx, message):
      textinput = message
      gs = goslate.Goslate()
      trans = gs.translate(textinput, 'en')
      embed = discord.Embed (title='Translation', description = f"Translation result: {trans}")
      embed.set_footer(text=f'Demandé par {ctx.message.author}. Message originale: {message}')
      await ctx.message.delete()
      await ctx.send(embed=embed) 
    
    @commands.command(brief = "Shows the amount of days left before Christmas Day.", description = 'Shows the amountof days before Christmas day. This command will be removed on 25/12/2022.')
    async def christmas(self, ctx):
      today = datetime.date.today()
      christmasday = datetime.date(2022,12,25)
      diff = christmasday - today
      embed = discord.Embed(title = 'Days left until Christmas.', description = f'Days left: `{diff.days} days`', colour = 0xFF0004)
      embed.set_footer(text=f'Requested by {ctx.message.author}.')
      await ctx.message.delete()
      await ctx.send(embed = embed)

    @commands.command(brief = 'Calculates progress through the year through a percentage.')
    async def yearprogress(self, ctx):
      today = datetime.datetime.now()
      date = today.date()   
      days = today.timetuple().tm_yday
      calc1 = days / 365
      calc2 = 365 - days
      percent = calc1 * 100
      percent = int(percent)
      year = date.strftime("%Y")
      year = int(year)
      nextyear = year + 1
      embed = discord.Embed(title = 'Year progress', description = f"We are `{percent}%` through the year! \n That means there's around `{calc2}` days left until {nextyear}", url="https://www.youtube.com/watch?v=pgXozIma-Oc", colour = 0x00FF0A)
      embed.set_footer(text = f'Requested by {ctx.message.author}. Current year: {year}')
      await ctx.message.delete()
      await ctx.send(embed = embed)


    @commands.command()
    async def vergil(self, ctx):
        await ctx.send('https://tenor.com/view/vergil-gif-25306498')

    @commands.command()
    async def rulesofnature(self, ctx):
        await ctx.send('https://tenor.com/view/metal-gear-rising-metal-gear-raiden-metal-gear-ray-super-strength-gif-14889306')

async def setup(client):
    await client.add_cog(Fun(client))
