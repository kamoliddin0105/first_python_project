from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "7931952441:AAHtRznahYQSHyzKZVpEplFejGf0JmkLmF4"

bot = telebot.TeleBot(TOKEN,parse_mode="None")

@bot.message_handler(commands=["start"])
def start(message):
    answer = "Welcome to lotin to kirill bot."
    answer += "\nEnter text:"
    bot.reply_to(message,answer)

@bot.message_handler(func=lambda message: True)
def translate(message):
    msg = message.text
    if msg.isascii():
        answer = to_cyrillic(msg)
    else:
        answer = to_latin(msg)
    bot.reply_to(message,answer)

bot.polling()