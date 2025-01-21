import discord
import os
# from os import listdir
from bs4 import BeautifulSoup
import json
import requests
# import search_runpee
# from discord.ext import commands
from dotenv import load_dotenv
from webscraping import searchGame
load_dotenv()

# TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Bot()

# if __name__=='__main__':
# 	"""Loads the cogs from the `./cogs` folder.
# 	Notes:
# 		The cogs are .py files.
# 		The cogs are named in this format `{cog_dir}.{cog_filename_without_extension}`_.
# 		"""
# 	for cog in listdir('./cogs'):
# 		if cog.endswith('.py') == True:
# 			bot.load_extension(f'cogs.{cog[:-3]}')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('games'))
    print(f"{bot.user} is ready and online!")

# @bot.slash_command(name="first_slash") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds. name="first_slash", guild_ids=[...]
# async def first_slash(ctx): 
#     await ctx.respond("You executed the slash command!")
@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "embedding", description = "Test embedding")
async def embed(ctx):
    embed = discord.Embed(
        title = "Embed Title",
        description="this is a description",
        color=discord.Colour.blue())
    await ctx.respond(embed=embed)

# @bot.slash_command(name='search', description='Search for a video game', guild_ids=[522178936092753932])
# async def search(ctx, name):
#     url = "https://www.igdb.com/games/" + name
#     html = request.urlopen(url).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     site_json = json.loads(soup.text)
#     await ctx.respond()
#     # await ctx.send('Hello ' + name + '!')
    
@bot.slash_command(name="search", description="Search for a video game")
async def search(ctx, search=None):
    fetchedGame = searchGame(search)
    # formattedGames = 
    await ctx.respond(fetchedGame)


bot.run(os.getenv('DISCORD_TOKEN'))