import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7785376105:AAEPeFWk6Vm7RrVdjf1Bjxrbd3IIleiYY_g"
OWNER_ID = 8091838884  # Owner'ning Telegram ID'si

bot = telebot.TeleBot(TOKEN)

user_languages = {}  # Foydalanuvchilar tanlagan tillarni saqlash uchun
user_messages = {}  # Foydalanuvchi ID bilan bog‘liq xabarlar

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("O'zbek 🇺🇿"), KeyboardButton("Русский 🇷🇺"), KeyboardButton("English 🇬🇧"))
    bot.send_message(message.chat.id, "Tilni tanlang | Выберите язык | Choose a language", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["O'zbek 🇺🇿", "Русский 🇷🇺", "English 🇬🇧"])
def set_language(message):
    user_languages[message.chat.id] = message.text
    responses = {
        "O'zbek 🇺🇿": "Salom! Nima yordam bera olaman?",
        "Русский 🇷🇺": "Привет! Чем могу помочь?",
        "English 🇬🇧": "Hello! How can I help you?"
    }
    bot.send_message(message.chat.id, responses[message.text])

@bot.message_handler(content_types=["text", "video", "document", "voice", "audio", "sticker"])
def forward_to_owner(message):
    if message.chat.id != OWNER_ID:
        user_messages[message.message_id] = message.chat.id  # Xabarni saqlash
        bot.forward_message(OWNER_ID, message.chat.id, message.message_id)
        bot.send_message(OWNER_ID, f"User ID: {message.chat.id}")
        bot.send_message(message.chat.id, "Xabaringiz yuborildi ✅")

@bot.message_handler(func=lambda message: message.reply_to_message is not None and message.chat.id == OWNER_ID,
                     content_types=["text", "video", "document", "voice", "audio", "sticker"])
def reply_to_user(message):
    try:
        original_message_id = message.reply_to_message.message_id
        user_id = user_messages.get(original_message_id)  # Asl foydalanuvchi ID sini olish
        if user_id:
            bot.copy_message(user_id, OWNER_ID, message.message_id)
            bot.send_message(OWNER_ID, "Javob foydalanuvchiga yuborildi ✅")
        else:
            bot.send_message(OWNER_ID, "Xatolik: Foydalanuvchini aniqlab bo‘lmadi.")
    except Exception as e:
        bot.send_message(OWNER_ID, f"Xatolik yuz berdi: {e}")

bot.polling(none_stop=True)
