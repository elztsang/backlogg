from igdb.wrapper import IGDBWrapper
import os
import json
from dotenv import load_dotenv
load_dotenv()

wrapper = IGDBWrapper(os.getenv('CLIENT_TOKEN'), os.getenv('ACCESS_TOKEN'))

# with a wrapper instance already created
# JSON API request
byte_array = wrapper.api_request(
            'games',
            'fields id, name; offset 0; where platforms=48;'
          )
# parse into JSON however you like...
parsed_json = json.loads(bytes)
# Print the parsed JSON for testing purposes
print(parsed_json)


# Protobuf API request
from igdb.igdbapi_pb2 import GameResult
byte_array = wrapper.api_request(
            'games.pb', # Note the '.pb' suffix at the endpoint
            'fields id, name; offset 0; where platforms=48;'
          )
games_message = GameResult()
games_message.ParseFromString(byte_array) # Fills the protobuf message object with the response
from igdb.wrapper import IGDBWrapper
import os
import json
from dotenv import load_dotenv
load_dotenv()

wrapper = IGDBWrapper(os.getenv('CLIENT_TOKEN'), os.getenv('ACCESS_TOKEN'))

# with a wrapper instance already created
# JSON API request
byte_array = wrapper.api_request(
            'games',
            'fields id, name; offset 0; where platforms=48;'
          )
# parse into JSON however you like...
parsed_json = json.loads(bytes)
# Print the parsed JSON for testing purposes
print(parsed_json)


# Protobuf API request
from igdb.igdbapi_pb2 import GameResult
byte_array = wrapper.api_request(
            'games.pb', # Note the '.pb' suffix at the endpoint
            'fields id, name; offset 0; where platforms=48;'
          )
games_message = GameResult()
games_message.ParseFromString(byte_array) # Fills the protobuf message object with the response