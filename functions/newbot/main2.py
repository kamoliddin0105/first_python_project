import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = "7785376105:AAEPeFWk6Vm7RrVdjf1Bjxrbd3IIleiYY_g"
OWNER_ID = 8091838884

bot = telebot.TeleBot(API_TOKEN)

users = {}

message_types = ["text", "video", "document", "voice", "audio", "sticker"]


@bot.message_handler(commands=["start"])
def start_command(message):
    user_id = message.from_user.id
    username = message.from_user.username if message.from_user.username else f"User_{user_id}"

    if user_id not in users:
        users[user_id] = {"username": username, "language": None}

        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(KeyboardButton("🇺🇿 O'zbekcha"), KeyboardButton("🇷🇺 Русский"), KeyboardButton("🇬🇧 English"))

        bot.send_message(user_id, "Iltimos, tilni tanlang:\n\n🇺🇿 O'zbekcha\n🇷🇺 Русский\n🇬🇧 English",
                         reply_markup=markup)
    else:
        bot.send_message(user_id, "Salom! Siz botdan foydalanyapsiz.")


@bot.message_handler(func=lambda message: message.text in ["🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇬🇧 English"])
def set_language(message):
    user_id = message.from_user.id
    if user_id in users and users[user_id]["language"] is None:
        lang = message.text
        if lang == "🇺🇿 O'zbekcha":
            users[user_id]["language"] = "uz"
            bot.send_message(user_id, "Assalomu alaykum! Sizni bu yerda ko‘rib turganimdan xursandman!")
        elif lang == "🇷🇺 Русский":
            users[user_id]["language"] = "ru"
            bot.send_message(user_id, "Привет! Рад видеть тебя здесь!")
        elif lang == "🇬🇧 English":
            users[user_id]["language"] = "en"
            bot.send_message(user_id, "Hi there! I’m glad to see you here!")

        bot.send_message(OWNER_ID,
                         f"🔔 Yangi foydalanuvchi: @{users[user_id]['username']} (ID: {user_id}), til: {users[user_id]['language']}")

        bot.send_message(user_id, "Qanday yordam bera olaman?", reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(func=lambda message: message.from_user.id == OWNER_ID)
def forward_to_owner(message):
    if message.from_user.id != OWNER_ID:
        user_id = message.from_user.id
        username = users.get(user_id, {}).get("username", f"User_{user_id}")

        bot.send_message(OWNER_ID, f"📩 Yangi xabar @{username} (ID: {user_id}):")
        bot.forward_message(OWNER_ID, user_id, message.message_id)
        bot.send_message(user_id, "✅ Xabaringiz jo‘natildi.")


@bot.message_handler(func=lambda message: message.from_user.id != OWNER_ID)
def reply_to_user(message):
    if message.from_user.id == OWNER_ID and message.reply_to_message:
        reply_text = message.reply_to_message.text
        for user_id, user_data in users.items():
            if f"@{user_data['username']}" in reply_text or f"(ID: {user_id})" in reply_text:
                bot.forward_message(user_id, OWNER_ID, message.message_id)
                bot.send_message(OWNER_ID, "✅ Xabaringiz foydalanuvchiga jo‘natildi.")
                return

    bot.send_message(OWNER_ID, "❌ Foydalanuvchini aniqlab bo‘lmadi.")


bot.polling(none_stop=True)
