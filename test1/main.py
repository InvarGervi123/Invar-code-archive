import discord
from discord.ext import commands
import random
import asyncio
import texts
import openai
good_words = ["ישמנה",
            "השמנת",
            "כמה את אוכלת?",
            "זה כל מה שהבאת לאכול?",
            "יאנורקסית",
            "ימכוערת",
            "רזית",
            "יזנה",
            "שרמטה",
            "מה את לובשת?",
            "בעיה שלך שלבשת את זה",
            "מה לבשת כשזה קרה?",
            "נו כל אחת מוטרדת אל תתלהבי"]

woohoo_words = ["⡄⠀⠀⠀⢀⣼⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢷⣄⠀⠀⠀⠈⠙⣦⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⣠⣿⣿⠟⠉⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢆⠀⠀⠀⠀⠈⠳⡀⠀⠀⠀⠀",
                "⠀⠀⣰⡿⠋⢡⡔⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀",
                "⠀⣰⠋⠀⣀⠔⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣶⣤⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠈⢆⠀⠀",
                "⣰⠃⠀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠋⠉⠉⠀⠒⠂⠀⠀⠠⣌⡇⠀⠀⠀⠀⠀⠈⢆⠀",
                "⠃⠀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠈⢦",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠴⠚⠉⠁⣀⠠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠈",
                "⠀⠀⠀⠀⠀⠀⢀⠔⠉⠀⠀⠀⠀⠁⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠐⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣮⣿⣿⣿⣷⣾⣵⣦⡖⠀⢀⣼⠀⠀⠀⠀⠀⣠⣾",
                "⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢤⣶⣖⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠟⢻⡛⠛⠿⠉⠉⠙⠛⠻⣿⠯⢿⠀⠀⠀⢀⡴⢻⣿",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣶⣿⣿⣿⠛⠿⠶⠂⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠈⠑⠂⠀⠀⠀⠀⠀⠁⠀⣾⣆⠀⢀⣾⣽⣿⡟",
                "⠀⠀⠀⠀⠀⠀⠀⠀⢲⣶⣾⠟⠋⠙⠯⢍⣀⡀⠤⠄⠀⠀⠀⠀⠀⠀⠀⠺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠘⡄⢸⣿⠁⣿⢡",
                "⠀⠀⠀⠀⠀⠀⠤⣴⣿⢋⠀⠀⢀⡤⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠸⣼⣿⣼⣣⣿",
                "⠀⠀⠀⠀⠀⠐⠚⠛⠉⠁⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢣⢀⢿⣿⣿⣿⣿",
                "⠀⠀⢀⡠⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⠀⢸⣼⣿⣟⣻⣿⣿",
                "⠈⠻⣅⡀⣀⡀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠐⢄⠀⠀⠀⠀⢸⡏⠉⠉⠁⠈⠉",
                "⢆⠀⠈⠳⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣜⢁⣀⡌⣿⣄⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⢸⠇⠀⠀⠀⠀⠀",
                "⠈⠓⢤⡀⠀⢿⡒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⢻⣦⠀⡞⠀⠀⠀⠀⠀⠀",
                "⠀⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⢃⡿⠁⠀⠀⠀⠀⠀⠀",
                "⠀⠀⢼⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡿⢿⢻⣿⡇⠀⠀⠀⠀⠀⠀⡼⠁⠀⢀⡄⠀⠀⠀⠀",
                "⠀⠀⠀⢙⣶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠉⠀⠨⣿⡀⠀⠸⢿⡇⠀⠀⠀⠀⠀⡜⠁⠀⣠⡞⠀⠀⠀⠀⠀",
                "⣆⡀⠀⠀⠉⠛⠀⠐⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠈⢷⠀⠀⠀⢃⠀⠀⠀⢀⡞⠀⢀⣴⠏⠀⠀⠀⠀⠀⠀",
                "⠀⠙⠒⠤⢤⣀⣀⣀⣈⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠈⡆⠀⠀⢸⠀⠀⢠⠎⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠘⠾⡇⠉⢻⣷⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⡀⠀⠀⢸⠀⠀⡀⠀⢠⠏⢀⠼⠋⠄⠀⠀⠀⠀⠀⠀⠀⠘",
                "⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢷⡀⠉⠒⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀⠘⠀⠀⡇⢀⡎⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
                "⢃⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢆⠀⠀⠙⢿⣶⣤⡀⠀⡀⠀⠀⠀⠀⠀⠙⡀⠀⠀⢰⢁⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
                "⢸⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⠀⠻⣿⣷⣀⣽⣷⣶⣦⡤⠤⢄⣵⠄⠤⠞⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀"]

rick_roll_words = []

food_texts = "קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית קציצה אוטיסטית"





# Discord bot token
TOKEN = 'MTExMTk2NjIzODA3MjEyNzU0OA.Gc21B5.BUqH-YLSwPwX_1kek3CmCJF017fvCpxor_T62Y'

# Create a new Discord bot instance
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

AUTHORIZED_USER_ID = 931958595065634837

# Event triggered when the bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')
   # await send(f'שלום , קורים לי שונית. אני מוכנה להכין להכם שקשוקה')

import requests

def get_weather_forecast(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Можете изменить на "imperial" для температуры в Фаренгейтах.
    }

  #  try: 2024IDK
  #      response = requests.get(base_url, params=params)
   #     data = response.json()
#
 #       if response.status_code == 200:  2024IDK
  #          weather_description = data["weather"][0]["description"]
 #           temperature = data["main"]["temp"]
  #          humidity = data["main"]["humidity"]
#            return f"Погода в городе {city}: {weather_description}, Температура: {temperature}°C, Влажность: {humidity}%."
 #       else:
 #           return f"Не удалось получить прогноз погоды. Код ошибки: {response.status_code}"
 #   except Exception as e:
 #       return f"Произошла ошибка: {e}"
#
#if __name__ == "__main__":
#    api_key = "ВАШ_API_КЛЮЧ"  # Замените на свой ключ API OpenWeatherMap
#    city_name = input("Введите название города: ")
 #   forecast = get_weather_forecast(city_name, api_key)
 #   print(forecast)  2024IDK


import time as t
class Gun():
    magazin = False
    twice = [3]
    auto_reset = True
    async def Recharge(message):
        global magazin
        await message.channel.send(f'{"Recharge"}') ##########################
        for i in Gun.twice:
            t.sleep(150)
            await message.channel.send(f'{"."}')
        print("\n") ################################
        magazin = True
        await message.channel.send(f'{"FULL"}') ##############################

    async def Reset(message):
        global magazin
        if magazin == False:
            Gun.Recharge(message)
        else:
            await message.channel.send(f'{"WAS FULL"}') #####################
    
    async def Auto_Reset_Shoot(message):
        global magazin
        if magazin == False:
            await message.channel.send(f'{"MAGAZIN IS NOT FULL"}') ###########
            if Gun.auto_reset == True:
                Gun.Recharge(message)
                Gun.Shoot(message)

    async def Shoot(message):
        global magazin
        await message.channel.send(f'{"BOOM"}') ##############################
        for i in Gun.twice:
            t.sleep(100)
            await message.channel.send(f'{" BOOM"}') #########################
        print("\n") ################################
        magazin = False

openai.api_key = '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'   #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 #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

# Функция для взаимодействия с моделью
def interact_with_gpt3(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Используйте нужный вам движок модели GPT-3.5
        prompt=prompt,
        max_tokens=100,  # Максимальное количество токенов в ответе
        temperature=0.7,  # Коэффициент температуры для вариативности ответов
        n=1,  # Количество генерируемых ответов
        stop=None,  # Опциональное условие остановки для генерации
    )

    # Получение ответа от модели
    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None

gun = Gun
@bot.event
async def on_message(message):
    #if command == "s":
    #   gun.Auto_Reset_Shoot(message)
    #elif command == "r":
    #    gun.Reset(message)
    #elif command == "ar":
    #    if gun.auto_reset:
    #        gun.auto_reset = False
    #        print("AUTO Recharge off") ##############
    #    else:
    #        gun.auto_reset = True
    #        print("AUTO Recharge on") ###############
    #if message.content.startswith(): ##################################
    #    commands = message#.




# Event triggered when a message is received

    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return


    # Check if the message starts with a specific command
    if message.content.startswith('q'):
        # Ask a question
        question = 'מה צבע הקקי האוהב הצלך?'

        # Possible answers
        answers = ['כושי', 'ממש כושי', 'ULTRA כושי', 'לוטן', 'זין של תמי']

        # Generate a random answer
        answer = random.choice(answers)

        # Send the question and answer to the same channel
        await message.channel.send(f'שאלה: {question}\nתוצאה: {answer}')
    start_help ='יכולת לשתמש בי כמו בובת מין פה:'
    if message.content.startswith('תמי'):
        for i in range(5):
            await message.channel.send(f'https://cdn.discordapp.com/attachments/1092514600865513643/1112014985783156786/MemeKing.png')
    memes = ['https://cdn.discordapp.com/attachments/766983081155493888/1066390586254446643/meme_of_me_school_fixed_2.png','https://cdn.discordapp.com/attachments/766983081155493888/1039058246268354600/ULTRA_ILAN_HAMMI_2.png','https://cdn.discordapp.com/attachments/766983081155493888/1029397025625755739/unknown.png','https://cdn.discordapp.com/attachments/766983081155493888/1029003164919271445/flag-1.png','https://cdn.discordapp.com/attachments/766983081155493888/1027184426817433610/Untitled-1-Recovered_hub.png','https://cdn.discordapp.com/attachments/766983081155493888/1024299490762575933/unknown.png','https://cdn.discordapp.com/attachments/766983081155493888/1018926467016577154/Ilan_hammi_gay_party.png','https://cdn.discordapp.com/attachments/766983081155493888/1018588171749036103/rahel_and_herzel_drive_small_png.png','https://cdn.discordapp.com/attachments/766983081155493888/1018449926193172520/shounit_war2.png','https://cdn.discordapp.com/attachments/766983081155493888/1018153790525943879/shunit_marvel.png']
    if message.content.startswith('memes'):
        meme = random.choice(memes)
        await message.channel.send(f'{meme}')
    if message.content.startswith('/help'):
        await message.channel.send(f'{start_help}woohoo,gf,זין,סרטן,q,תמי,memes,כושי,טענה ונימוק,בדיקת חיים של לוטן')
    if message.content.startswith('כושי'):
        for i in range(10):
            await message.channel.send(f' לוטן כושי במקום {10-i}')
    if message.content.startswith('טענה ונימוק' or 'בדיקת חיים של לוטן'):
        await message.channel.send(f'https://cdn.discordapp.com/attachments/766983081155493888/953745681200324648/1.png')
    if message.content.startswith('סרטן'):
        await message.channel.send(f'https://cdn.discordapp.com/attachments/766983081155493888/1112712544193368124/ezgif.com-video-to-gif_3.gif')
    if message.content.startswith('זין'):
        for i in range(3):
            await message.channel.send(f'{message.author.mention}זונה')
    if message.content.startswith('gf'):
        answer = random.choice(good_words)
        await message.channel.send(f'{answer}')
    if message.content.startswith('woohoo'):
        for i in woohoo_words:
            await message.channel.send(f'{i}')

    if message.content.startswith('לוטן'):
        for i in range(2):
            await message.channel.send(f'{food_texts}') 

    if message.content.startswith('!question'):
        # Ask a question
        question = 'What is your favorite color?'

        # Send the question to the same channel
        question_message = await message.channel.send(f'Question: {question}')

        # Wait for a response from the authorized user
        def check_author(m):
            return m.author.id == AUTHORIZED_USER_ID and m.channel == message.channel

        try:
            response = await bot.wait_for('message', check=check_author, timeout=60)
        except asyncio.TimeoutError:
            await message.channel.send('No response received. Time limit exceeded.')
            return

        # Get the answer from the response message
        answer = response.content

        # Send the answer to the same channel
        await message.channel.send(f'Answer: {answer}')
    
    if message.content.startswith('!shunit'):
        # Ask a question
        question = 'DO YOU GAY?'

        # Send the question to the same channel
        question_message = await message.channel.send(f'Question: {question}')
      
        # Wait for a response from the authorized user
        def check_author(m):
            return m.author.id == AUTHORIZED_USER_ID or m.channel == message.channel

        try:
            response = await bot.wait_for('message', check=check_author, timeout=60)
        except asyncio.TimeoutError:
            await message.channel.send('No response received. Time limit exceeded.')
            await bot.process_commands(message)  # Process other commands
            return

        # Get the answer from the response message
        answer = response.content

        # Send the answer to the same channel
        await message.channel.send(f'Answer: {answer}')
        response = interact_with_gpt3(answer)
        await message.channel.send(f'YOU ARE GAY, {response}') 


    await bot.process_commands(message)  # Process other commands


        #user_input = message.content.startswith()
        #response = interact_with_gpt3(answer)
        #await message.channel.send(f'{response}') 
        


    await bot.process_commands(message)
    

# Run the bot
bot.run(TOKEN)
