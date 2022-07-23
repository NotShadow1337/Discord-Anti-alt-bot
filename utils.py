#libraries
import json

#configuration
with open('config.json') as f:
    config = json.load(f)
    token = config['token']
    guild_id = config['guild_id']
    success_emoji = config['emojis']['success']
    error_emoji = config['emojis']['failure']

#Anti-alt functions
def set_minimum_days(days):
    with open('database.json', 'r') as f:
        database = json.load(f)
    database['minimum-days'] = days
    with open('database.json', 'w') as f:
        json.dump(database, f, indent = 4)

def get_minimum_days():
    with open('database.json', 'r') as f:
        database = json.load(f)
    return database['minimum-days']

def set_log_channel(channel):
    with open('database.json', 'r') as f:
        database = json.load(f)
    database['log-channel'] = channel
    with open('database.json', 'w') as f:
        json.dump(database, f, indent = 4)

def get_log_channel():
    with open('database.json', 'r') as f:
        database = json.load(f)
    return database['log-channel']