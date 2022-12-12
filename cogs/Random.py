import discord
from discord.ext import commands
from discord import app_commands
import random
from random import choice

class Random(commands.Cog):

    def __init__(self, client):
        self.dlient = client

#    @commands.command()
#    async def yesno(self, ctx):
#        yesno = choice(["Yes", "No", "Maybe"])
#        await ctx.send(yesno)

#    @commands.command(brief = "Going against it's answers is heresy.")
    @app_commands.command(name='8ball', description="Going against it's answers is heresy.")
    @app_commands.describe(message = "Question")
    async def eightball(self, interaction: discord.Interaction, message: str = None):
        pick = choice(["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."])
        if message != None:
            Originalmessage = f'Original message: {message}'
        else:
            Originalmessage = 'No question specified.'
        embed = discord.Embed(title = '8ball', description = pick)
        embed.set_footer(text=f"Requested by {interaction.user.name}. {Originalmessage}")
        await interaction.response.send_message(embed=embed)

#    @commands.command()
#    async def rng(self, ctx):
#        rng = random.randint(1, 1000)
#        embed = discord.Embed(title='Random Number Generator (1-1000)', description = rng, colour=0x00FF5E)
#        await ctx.send(embed=embed)
#    @commands.command(brief='Throws out a random number depending on your input.', description='This command outputs a random number between 1 and what you inputted. Inputing nothing will default to a value of 1000.')

    @app_commands.command(name = 'rng', description="Picks a random number between 1 and the number you specify. Defaults to 1000 if not sepcified")
    @app_commands.describe(message = "Number")
    async def rng(self, interaction:discord.Interaction, message: int = 1000):
        choice = int(message)
        rngnumber = random.randint(1, choice)
        embed = discord.Embed (title='RNG', description = f'You got `{rngnumber}`')
        embed.set_footer(text=f'Requested by {interaction.user.name}. RNG range: 1-{choice}')
        await interaction.response.send_message(embed=embed)


async def setup(client):
    await client.add_cog(Random(client))
