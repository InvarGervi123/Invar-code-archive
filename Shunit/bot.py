import discord
import json
from discord.ext import commands
import responses

#yossi = 1111993470656188446





async def send_messages(message, user_message):
    try:
        response = responses.handle_responses(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = "MTExMTk2NjIzODA3MjEyNzU0OA.Gc21B5.BUqH-YLSwPwX_1kek3CmCJF017fvCpxor_T62Y"

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
