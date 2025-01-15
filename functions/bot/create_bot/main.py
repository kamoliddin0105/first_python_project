import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from functions.bot.my_telegram_bot.data import regions, products

TOKEN = "7785376105:AAEPeFWk6Vm7RrVdjf1Bjxrbd3IIleiYY_g"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("Option 1",callback_data="option1")
    btn2 = InlineKeyboardButton("Option 2",callback_data="option2")
    btn3 = InlineKeyboardButton("Option 3",callback_data="option3")
    markup.add(btn1,btn2,btn3)

    bot.send_message(message.chat.id,"Choose an option:",reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "option1":
        bot.send_message(call.message.chat.id,"Option 1")
    elif call.data == "option2":
        bot.send_message(call.message.chat.id,"Option 2")
    elif call.data == "option3":
        bot.send_message(call.message.chat.id,"Option 3")

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("Option 1")
    btn2 = KeyboardButton("Option 2")
    btn3 = KeyboardButton("Option 3")
    btn4 = KeyboardButton("Option 4")
    btn5 = KeyboardButton("Option 5")
    btn6 = KeyboardButton("Option 6")
    btn7 = KeyboardButton("Option 7")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    bot.send_message(message.chat.id, "Choose", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def reply_handler(message):
    if message.text == "Option 1":
        bot.send_message(message.chat.id, "You selected Option 1")
    elif message.text == "Option 2":
        bot.send_message(message.chat.id, "You selected Option 2")
    else:
        bot.send_message(message.chat.id, "Please selected a valid option")

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


# Another bot


user_cart = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}!")

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    contact_button = KeyboardButton("📞 Kontakt yuborish", request_contact=True)
    markup.add(contact_button)

    bot.send_message(message.chat.id, "Kontaktingizni yuboring", reply_markup=markup)


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if message.contact is not None:
        with open("/Users/macbook/PycharmProjects/first_python_project/functions/bot/create_bot/files/contacts.txt",
                  "a") as file:
            file.write(f"{message.contact.first_name} - {message.contact.phone_number}\n")
            bot.send_message(message.chat.id,
                             f"Rahmat {message.contact.first_name}! Sizning telefon raqamingiz qabul qilindi va saqlandi")

            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            location_button = KeyboardButton("📍 Lokatsiyani ulashish", request_location=True)
            markup.add(location_button)
            bot.send_message(message.chat.id, "Endi lokatsiyangizni ulashing:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Kontakt ma'lumotlari qabul qilinmadi. Iltimos, qaytadan urinib ko'ring.")


@bot.message_handler(content_types=['location'])
def handle_location(message):
    if message.location is not None:
        lat = message.location.latitude
        lon = message.location.longitude

        with open("/Users/macbook/PycharmProjects/first_python_project/functions/bot/create_bot/files/location.txt",
                  "a") as file:
            file.write(f"Latitude: {lat}, Longitude: {lon}\n")
            bot.send_message(message.chat.id,
                             "Rahmat! Sizning lokatsiyangiz saqlandi va qabul qilindi.")

            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for region in regions:
                markup.add(KeyboardButton(region))
            bot.send_message(message.chat.id, "Iltimos, quyidagi hududlardan birini tanlang:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Lokatsiya ma'lumotlari qabul qilinmadi. Iltimos, qaytadan urinib ko'ring.")

@bot.message_handler(func=lambda message: message.text in regions)
def handle_countries(message):
    region = message.text
    with open("/Users/macbook/PycharmProjects/first_python_project/functions/bot/create_bot/files/region.txt", "a") as file:
        file.write(f"region - {region}\n")
    bot.send_message(message.chat.id, "Rahmat! Sizning hududingiz qabul qilindi va saqlandi.")

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for category in products.keys():
        markup.add(KeyboardButton(category))

    bot.send_message(message.chat.id, "Iltimos quyidagi kategoriyalardan birini tanlang.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in products.keys())
def handle_categories(message):
    product = message.text
    if product in products:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for item in products[product]:
            markup.add(KeyboardButton(item))
        bot.send_message(message.chat.id, "Iltimos, quyidagi mahsulotlardan birini tanlang:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Mahsulot qabul qilinmadi. Iltimos, qaytadan urinib ko'ring.")


user_cart = {}

@bot.message_handler(func=lambda message: any(message.text in sublist for sublist in products.values()))
def handle_product_selection(message):
    selected_product = message.text

    if selected_product not in user_cart:
        user_cart[selected_product] = 1

    inline_markup = InlineKeyboardMarkup()
    inline_markup.row(
        InlineKeyboardButton("➖", callback_data=f"decrease_{selected_product}"),
        InlineKeyboardButton(f"{user_cart[selected_product]}", callback_data="quantity_display"),
        InlineKeyboardButton("➕", callback_data=f"increase_{selected_product}")
    )
    inline_markup.add(InlineKeyboardButton("🛒 Sotib olish", callback_data=f"buy_{selected_product}"))

    product_image_path = f"/Users/macbook/PycharmProjects/first_python_project/functions/bot/create_bot/images/{selected_product}.jpg"
    try:
        with open(product_image_path, "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption=f"Siz tanlagan mahsulot: {selected_product}", reply_markup=inline_markup)
    except FileNotFoundError:
        bot.send_message(message.chat.id, f"Siz tanlagan mahsulot: {selected_product}\nAfsuski, ushbu mahsulot rasmi mavjud emas.", reply_markup=inline_markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith(("increase_", "decrease_", "buy_")))
def handle_quantity_buttons(call):
    user_id = call.message.chat.id
    product_name = call.data.split("_")[1]

    if call.data.startswith("increase_"):
        user_cart[product_name] += 1
    elif call.data.startswith("decrease_"):
        if user_cart[product_name] > 1:
            user_cart[product_name] -= 1
    elif call.data.startswith("buy_"):
        quantity = user_cart[product_name]
        bot.send_message(user_id, f"Rahmat! Siz {quantity} dona {product_name} sotib olishni tanladingiz. Operator siz bilan tez orada bog'lanadi.")
        return

    inline_markup = InlineKeyboardMarkup()
    inline_markup.row(
        InlineKeyboardButton("➖", callback_data=f"decrease_{product_name}"),
        InlineKeyboardButton(f"{user_cart[product_name]}", callback_data="quantity_display"),
        InlineKeyboardButton("➕", callback_data=f"increase_{product_name}")
    )
    inline_markup.add(InlineKeyboardButton("🛒 Sotib olish", callback_data=f"buy_{product_name}"))

    bot.edit_message_reply_markup(chat_id=user_id, message_id=call.message.message_id, reply_markup=inline_markup)





bot.polling()
