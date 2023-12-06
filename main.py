import discord
from core import CustomBot

from os import getenv
from dotenv import load_dotenv

load_dotenv()
CustomBot(command_prefix="!", intents=discord.Intents.all()).run(getenv('TOKEN'))