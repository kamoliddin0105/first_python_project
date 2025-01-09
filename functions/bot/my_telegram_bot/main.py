import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from data import regions, products, product_images

TOKEN = "7742773923:AAGZnSWUMkNd9NS3yyoBCQw-A3EQeAnMhwE"
bot = telebot.TeleBot(TOKEN)

user_baskets = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact_button = KeyboardButton("📞 Kontaktni ulashish", request_contact=True)
    markup.add(contact_button)
    bot.send_message(message.chat.id, "Iltimos, kontakt ma'lumotlaringizni ulashing:", reply_markup=markup)


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if message.contact is not None:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        location_button = KeyboardButton("📍 Lokatsiyani ulashish", request_location=True)
        markup.add(location_button)
        bot.send_message(message.chat.id, "Endi lokatsiyangizni ulashing:", reply_markup=markup)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    if message.location:
        bot.send_message(message.chat.id, "Lokatsiyangizni qabul qildim.")
        send_region_selection(message)


def send_region_selection(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
    for region in regions:
        markup.add(KeyboardButton(region))
    bot.send_message(message.chat.id, "Iltimos, quyidagi xududlardan birini tanlang:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in regions)
def handle_region_selection(message):
    region = message.text
    bot.reply_to(message, f"Rahmat! Siz {region} xududini tanladingiz.")
    send_category_selection(message)


def send_category_selection(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    category_button_1 = KeyboardButton("🍽 Yeguliklar")
    category_button_2 = KeyboardButton("🍰 Shirinliklar")
    category_button_3 = KeyboardButton("🥤 Ichimliklar")
    markup.add(category_button_1, category_button_2, category_button_3)
    bot.send_message(message.chat.id, "Iltimos, quyidagi kategoriyalardan birini tanlang:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["🍽 Yeguliklar", "🍰 Shirinliklar", "🥤 Ichimliklar"])
def handle_category_selection(message):
    category = message.text
    bot.reply_to(message, f"Rahmat! Siz {category} kategoriyasini tanladingiz.")
    send_product_selection(message, category)


def send_product_selection(message, category):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for product in products[category]:
        markup.add(KeyboardButton(product))

    basket_button = KeyboardButton("🛒 Savatni ko'rish")
    back_button = KeyboardButton("🔙 Orqaga")
    markup.add(basket_button, back_button)

    bot.send_message(message.chat.id, f"Tanlangan kategoriya: {category}. Iltimos, mahsulotni tanlang:",
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in [item for sublist in products.values() for item in sublist])
def handle_product_selection(message):
    product = message.text
    image = product_images.get(product, "")

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("➕", callback_data=f"add_{product}"))
    markup.add(InlineKeyboardButton("➖", callback_data=f"remove_{product}"))
    markup.add(InlineKeyboardButton("🛒 Savatga qo'shish", callback_data=f"add_to_basket_{product}"))

    bot.send_photo(message.chat.id, image, caption=f"Mahsulot: {product}", reply_markup=markup)


@bot.callback_query_handler(
    func=lambda call: call.data.startswith("add_") or call.data.startswith("remove_") or call.data.startswith(
        "add_to_basket_"))
def handle_callback(call):
    user_id = call.from_user.id
    action, product = call.data.split("_", 1)

    if action == "add_to_basket":
        if user_id not in user_baskets:
            user_baskets[user_id] = []
        user_baskets[user_id].append(product)
        bot.answer_callback_query(call.id, f"{product} savatga qo'shildi!")

    elif action == "add" or action == "remove":
        # Mahsulotni savatga qo'shish yoki olib tashlash
        bot.answer_callback_query(call.id, f"{action.capitalize()} button: {product}")

    elif action == "basket":
        # Savatni ko'rish
        basket = user_baskets.get(user_id, [])
        basket_message = "\n".join(basket) if basket else "Savat bo'sh."
        bot.send_message(call.message.chat.id, f"Savatdagi mahsulotlar:\n{basket_message}")

    bot.delete_message(call.message.chat.id, call.message.message_id)


bot.polling()
