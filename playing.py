import os
import json
import random
import discord

"""
Picks a random playing message out of JSON files in the specified path.
"""

PLAYING_FOLDER = os.path.join('.', 'config', 'playing')

options = []

for file in os.scandir(PLAYING_FOLDER):
    if file.name[-5:] == '.json':
        with open(file.path, 'r') as f:
            options.extend(json.loads(f.read()))

option = random.choice(options)

if option['type'] == 'playing':
    activity_type = discord.ActivityType.playing
elif option['type'] == 'watching':
    activity_type = discord.ActivityType.watching
elif option['type'] == 'listening':
    activity_type = discord.ActivityType.listening
else:
    raise ValueError(f"No discord.ActivityType corresponds to type {option['type']}")

activity = discord.Activity(
    type=activity_type,
    name=option['value']
)
