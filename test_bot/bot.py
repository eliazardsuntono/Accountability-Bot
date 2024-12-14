import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Important parameters for the stuff
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='$', intents=intents)

# How to implement commands
@bot.command()
async def blah(ctx):
    await ctx.send('blah')

bot.run(TOKEN)
