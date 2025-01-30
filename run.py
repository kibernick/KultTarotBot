#!/usr/bin/env python3


## Runs in Linux via: python kultTarotBot.py
## Requires Python > 3.4
## Bot needs to be given message read and send permissions on the Discord server.
## Need to install the discord.py API wrapper (e.g., via: pip install discord.py)
##
## Discord Bot Token needs to be in a file called "tokenFile.txt" which sits in the same
## directory as this file.


import logging

from kult_tarot_bot.client import client
from kult_tarot_bot.utils import get_discord_token

MODE_FILE = "modeFile.txt"

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


if __name__ == "__main__":
    ## Run Bot on Discord server
    discord_token = get_discord_token(MODE_FILE, logger)
    client.run(discord_token)
