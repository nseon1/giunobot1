print(f"Starting bot...")


import csv


import time
startTime = time.time()

print(f"Importing modules...")
csv_file = 'insert your own file here'
csv_data = []

with open(csv_file, 'r', encoding="utf8", errors="ignore") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        csv_data.append(row)



import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import pickle
import os.path
import asyncio
#async
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())



print(f"Importing .env configuration...")



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot (command_prefix='!!',intents=intents)

#turning the csv file to array


# Now, csv_data is a list representing the values in the CSV column.

print(f"Startup complete!\t[ {(time.time()-startTime):.2f}s ]")

@bot.command(name='test')
async def getvalue(ctx, index: int):
    # Check if the provided index is within the valid range
    if 0 <= index < len(csv_data):
        value = csv_data[index]
        await ctx.send(f"{value}")
    else:
        await ctx.send(f"Index out of range. The valid range is from 0 to {len(csv_data) - 1}.")



bot.run(TOKEN)
