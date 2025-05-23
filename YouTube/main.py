import discord
from discord.ext import tasks
from googleapiclient.discovery import build

# Вставьте токен вашего Discord-бота здесь
DISCORD_BOT_TOKEN = "MTEzNTc5MDA5ODY0NzEwOTY5Mg.GmiPhi.h6ljlUZqd8mtjCHa1Iv_XGknPUCvRB78kbhZ6M"

intents = discord.Intents.default()

bot = discord.Client(intents=intents)




















# Запуск бота
bot.run(DISCORD_BOT_TOKEN)