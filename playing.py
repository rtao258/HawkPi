import os
import json
import random
import discord

PLAYING_FOLDER = os.path.join('.', 'config', 'playing')


def get_activity_type(activity_type: str):
    """
    Get discord.py ActivityType based on corresponding string.
    :param activity_type: A string that is either 'playing', 'watching', or 'listening'.
    :type: str
    :return: a discord.ActivityType .playing, .watching, or .listening
    :rtype: class
    """
    if activity_type == 'playing':
        return discord.ActivityType.playing
    elif activity_type == 'watching':
        return discord.ActivityType.watching
    elif activity_type == 'listening':
        return discord.ActivityType.listening
    else:
        raise ValueError(f"No discord.ActivityType corresponds to type {activity_type}")


def choose_activity(activities_folder=PLAYING_FOLDER):
    """
    Chooses an activity at random from the given folder.
    :param activities_folder: 
    :type: str, optional
    :return: a Discord activity
    :rtype: discord.Activity
    """
    options = []

    for file in os.scandir(activities_folder):
        if file.name[-5:] == '.json':
            with open(file.path, 'r') as f:
                options.extend(json.loads(f.read()))

    option = random.choice(options)

    activity_type = get_activity_type(option['type'])

    return discord.Activity(
        type=activity_type,
        name=option['value']
    )
