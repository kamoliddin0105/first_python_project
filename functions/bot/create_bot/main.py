import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7785376105:AAEPeFWk6Vm7RrVdjf1Bjxrbd3IIleiYY_g"

bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = InlineKeyboardMarkup()
#     btn1 = InlineKeyboardButton("Option 1",callback_data="option1")
#     btn2 = InlineKeyboardButton("Option 2",callback_data="option2")
#     btn3 = InlineKeyboardButton("Option 3",callback_data="option3")
#     markup.add(btn1,btn2,btn3)
#
#     bot.send_message(message.chat.id,"Choose an option:",reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data == "option1":
#         bot.send_message(call.message.chat.id,"Option 1")
#     elif call.data == "option2":
#         bot.send_message(call.message.chat.id,"Option 2")
#     elif call.data == "option3":
#         bot.send_message(call.message.chat.id,"Option 3")

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = KeyboardButton("Option 1")
#     btn2 = KeyboardButton("Option 2")
#     btn3 = KeyboardButton("Option 3")
#     btn4 = KeyboardButton("Option 4")
#     btn5 = KeyboardButton("Option 5")
#     btn6 = KeyboardButton("Option 6")
#     btn7 = KeyboardButton("Option 7")
#     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
#
#     bot.send_message(message.chat.id, "Choose", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: True)
# def reply_handler(message):
#     if message.text == "Option 1":
#         bot.send_message(message.chat.id, "You selected Option 1")
#     elif message.text == "Option 2":
#         bot.send_message(message.chat.id, "You selected Option 2")
#     else:
#         bot.send_message(message.chat.id, "Please selected a valid option")

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("BMW")
    btn2 = KeyboardButton("Mers")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Choose:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def cars(message):
    if message.text == "BMW":
        markup = choose_bmws_type()
        bot.send_message(message.chat.id, "Choose:", reply_markup=markup)
    elif message.text == "Mers":
        with open("/Users/macbook/PycharmProjects/first_python_project/functions/bot/create_bot/images/Mers.jpg",
                  "rb") as photo:
            bot.send_photo(message.chat.id, photo=photo, caption="Mers photo")
    elif message.text in ["BMW m3", "BMW m4", "BMW m5", "BMW i3"]:
        bmw_models(message)
    else:
        bot.send_message(message.chat.id, "Please a selected a valid option")


def choose_bmws_type():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("BMW m3")
    btn2 = KeyboardButton("Mers m4")
    btn3 = KeyboardButton("Mers m5")
    btn4 = KeyboardButton("Mers i3")
    markup.add(btn1, btn2, btn3, btn4)
    return markup


@bot.message_handler(commands=['BMW'])
def bmw_models(message):
    if message.text == "BMW m3":
        with open("/Users/macbook/PycharmProjects/first_python_project/functions/bot/create_bot/images/BMW.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo=photo, caption="BMW m3 photo")
    else:
        bot.send_message(message.chat.id, "Please a valid option")



bot.polling()
