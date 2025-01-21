import json
from json import loads
from webscraping import *
from json import loads
import datetime

json_list = []
category = []
platforms = []
release_date = 0
name = []
coverURL = []

# pattern matching
# focus on formatting/embedding a SINGLE game for now!!

#might need to loop through 2d array
def manageJSON(jsonData):
    data = json.loads(jsonData)
    for item in data:
        name = item['name']
        coverURL = item['cover_small']
        print(coverURL)
        category = item['category']
        platforms = item['platforms']
        release_date = item['first_release_date']
        release_date = datetime.datetime.fromtimestamp((release_date))
        print(f"{release_date:%Y-%m-%d}")
        


# use hashtable to match number values to their corresponding strings
# manageJSON(getSpecificGame(279337))



# {1: u'Apple', 2: u'Orange', 3: u'Grapes', 4: u'Banana', 5: u'Mango'}


