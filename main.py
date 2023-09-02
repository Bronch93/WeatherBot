import telebot
import requests
import json

bot = telebot.TeleBot("6647921728:AAFRs2s_xi3kpx9lC498jBzN86DmqtbIU2A")
API ='3d9de74844d28377e81415151cbe6a66'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, enter the City")
    

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        wind = data["wind"]["speed"]
        bot.reply_to(message, f'Temperature: {temp} °C \nClouds: {weather} \nWindspeed: {wind} mi/s')
    else:
        bot.reply_to(message, 'City FAULT')

    
bot.polling(none_stop=True)
