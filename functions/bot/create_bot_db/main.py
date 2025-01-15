# import sqlite3
#
# # Ma'lumotlar bazasini yaratish
# def init_db():
#     conn = sqlite3.connect("bot_data.db")
#     cursor = conn.cursor()
#
#     # Kontaktlar uchun jadval
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS contacts (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             first_name TEXT,
#             phone_number TEXT
#         )
#     """)
#
#     # Lokatsiyalar uchun jadval
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS locations (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             latitude REAL,
#             longitude REAL
#         )
#     """)
#
#     # Regionlar uchun jadval
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS regions (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             region_name TEXT
#         )
#     """)
#
#     conn.commit()
#     conn.close()
#
# # Jadvalni yaratish uchun init_db funksiyasini chaqiramiz
# init_db()
#
# import telebot
# from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
# import sqlite3
#
# from functions.bot.my_telegram_bot.data import regions, products
#
# TOKEN = "7785376105:AAEPeFWk6Vm7RrVdjf1Bjxrbd3IIleiYY_g"
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, f"Salom, {message.from_user.first_name}!")
#
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     contact_button = KeyboardButton("📞 Kontakt yuborish", request_contact=True)
#     markup.add(contact_button)
#
#     bot.send_message(message.chat.id, "Kontaktingizni yuboring", reply_markup=markup)
#
#
# @bot.message_handler(content_types=['contact'])
# def handle_contact(message):
#     if message.contact is not None:
#         # Kontaktni ma'lumotlar bazasiga saqlash
#         conn = sqlite3.connect("bot_data.db")
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO contacts (first_name, phone_number) VALUES (?, ?)",
#                        (message.contact.first_name, message.contact.phone_number))
#         conn.commit()
#         conn.close()
#
#         bot.send_message(message.chat.id, f"Rahmat {message.contact.first_name}! Sizning telefon raqamingiz saqlandi.")
#
#         markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#         location_button = KeyboardButton("📍 Lokatsiyani ulashish", request_location=True)
#         markup.add(location_button)
#         bot.send_message(message.chat.id, "Endi lokatsiyangizni ulashing:", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, "Kontakt ma'lumotlari qabul qilinmadi. Iltimos, qaytadan urinib ko'ring.")
#
#
# @bot.message_handler(content_types=['location'])
# def handle_location(message):
#     if message.location is not None:
#         # Lokatsiyani ma'lumotlar bazasiga saqlash
#         lat = message.location.latitude
#         lon = message.location.longitude
#
#         conn = sqlite3.connect("bot_data.db")
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO locations (latitude, longitude) VALUES (?, ?)", (lat, lon))
#         conn.commit()
#         conn.close()
#
#         bot.send_message(message.chat.id, "Rahmat! Sizning lokatsiyangiz saqlandi va qabul qilindi.")
#
#         markup = ReplyKeyboardMarkup(resize_keyboard=True)
#         for region in regions:
#             markup.add(KeyboardButton(region))
#         bot.send_message(message.chat.id, "Iltimos, quyidagi hududlardan birini tanlang:", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, "Lokatsiya ma'lumotlari qabul qilinmadi. Iltimos, qaytadan urinib ko'ring.")
#
#
# @bot.message_handler(func=lambda message: message.text in regions)
# def handle_countries(message):
#     region = message.text
#     # Regionni ma'lumotlar bazasiga saqlash
#     conn = sqlite3.connect("bot_data.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO regions (region_name) VALUES (?)", (region,))
#     conn.commit()
#     conn.close()
#
#     bot.send_message(message.chat.id, "Rahmat! Sizning hududingiz saqlandi.")
#
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     for category in products.keys():
#         markup.add(KeyboardButton(category))
#
#     bot.send_message(message.chat.id, "Iltimos quyidagi kategoriyalardan birini tanlang.", reply_markup=markup)
#
#
# @bot.message_handler(func=lambda message: message.text in products.keys())
# def handle_categories(message):
#     product = message.text
#     if product in products:
#         markup = ReplyKeyboardMarkup(resize_keyboard=True)
#         for item in products[product]:
#             markup.add(KeyboardButton(item))
#         bot.send_message(message.chat.id, "Iltimos quyidagi productlardan birini tanlang:", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, "Product qabul qilinmadi, Iltimos, qaytadan urinib ko'ring.")
#
#
# bot.polling()
