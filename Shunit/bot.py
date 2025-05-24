import discord
import json
from discord.ext import commands
import responses

#yossi = ######################





async def send_messages(message, user_message):
    try:
        response = responses.handle_responses(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    token = os.getenv("DISCORD_TOKEN")
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return

        username = str(msg.author)
        user_msg = str(msg.content)
        channel = str(msg.channel)

       # if msg.author.id == yossi:
       #     return

        await send_messages(msg, user_msg)

    client.run(TOKEN)
