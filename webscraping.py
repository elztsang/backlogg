import discord
from discord.ext import commands
import requests
import json
import pprint
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

headers = {
    'Client-ID': os.getenv('CLIENT_ID'),
    'Authorization': 'Bearer ' + os.getenv('ACCESS_TOKEN'),
    }

# class Search(commands.Cog):

#     def __init__(self, bot): # this is a special method that is called when the cog is loaded
#         self.bot = bot
def searchGame(gameName):
    # headers = {
    # 'Client-ID': os.getenv('CLIENT_ID'),
    # 'Authorization': 'Bearer ' + os.getenv('ACCESS_TOKEN'),
    # }
    data = 'fields name,category,platforms,first_release_date; search "' + gameName + '"; limit 10;'
    # data = 'fields name,category,platforms,first_release_date, cover_small; where id = 279337;'
    response = requests.post('https://api.igdb.com/v4/games', headers=headers, data=data)
    # print("Status Code", response.status_code)
    return response.text

    # also find way to get thumbnail of game. for main display
    #specify a "sort by" as optional parameter.

def getSpecificGame(gameID):
    # headers = {
    # 'Client-ID': os.getenv('CLIENT_ID'),
    # 'Authorization': 'Bearer ' + os.getenv('ACCESS_TOKEN'),
    # }
    # data = 'fields name,category,platforms,first_release_date; search "' + gameName + '"; limit 10;'
    data = 'fields name,category,platforms,first_release_date, genres.name; where id = ' + str(gameID) + ';'
    response = requests.post('https://api.igdb.com/v4/games', headers=headers, data=data)
    # print("Status Code", response.status_code)
    return response.text

# print(getSpecificGame(279337))
# headers = {
#     'Client-ID': os.getenv('CLIENT_ID'),
#     'Authorization': 'Bearer ' + os.getenv('ACCESS_TOKEN'),
#     'Accept': 'application/json'
# }

# data = 'fields name, country_name, gender, description; search "bridget"; limit 10;'

# response = requests.post('https://api.igdb.com/v4/characters', headers=headers, data=data)
# print("Status Code", response.status_code)
# print(response.text)