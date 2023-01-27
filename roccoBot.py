import os
import discord
from dotenv import load_dotenv
import dadJokes

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot connected")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    m = message.content
    print(m)
    print
    if m.startswith("r!"):
        m = m[2:]
        print(m)
        m = m.split()
        print(m[0])
        if m[0] == "dadjoke":
            if len(m) != 2:
                joke = dadJokes.getDadJoke()
            else:
                joke = dadJokes.getDadJoke(input = m[1])
            print(joke)
            await message.channel.send(joke)
            
            


client.run(TOKEN)
