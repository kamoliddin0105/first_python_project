import telebot
import pickle
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message

API_TOKEN = "7949836220:AAHE3-wsLp9L2-u8vxpYw5ZLXgOEpftDiSM"
OWNER_ID =  7902295595

bot = telebot.TeleBot(API_TOKEN)

users = {}

message_types = ["text", "video", "document", "voice", "audio", "sticker", "video_note","photo","animation"]

class MessagesDb:
    db_path = 'telegram.db'

    def __init__(self):
        self.message_ids = self._load_messages()

    def _load_messages(self):
        try:
            with open(self.db_path, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {}

    def _update_db(self):
        with open(self.db_path, "wb") as file:
            file.write(pickle.dumps(self.message_ids))

    def add_message_id(self, message_id: int, user_id: int):
        self.message_ids[message_id] = user_id
        self._update_db()

    def get_message(self, message_id: int):
        return self.message_ids[message_id]

db = MessagesDb()

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
        bot.send_message(user_id,
                         "Salom! Siz botdan foydalanyapsiz.")


@bot.message_handler(func=lambda message: message.text in ["🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇬🇧 English"])
def set_language(message):
    user_id = message.from_user.id
    if user_id in users and users[user_id]["language"] is None:
        lang = message.text
        if lang == "🇺🇿 O'zbekcha":
            users[user_id]["language"] = "uz"
            bot.send_message(user_id, "Assalomu alaykum! Sizni bu yerda ko‘rib turganimdan xursandman! \n"
                                      "Qanday yordam bera olaman?",
                             reply_markup=telebot.types.ReplyKeyboardRemove())
        elif lang == "🇷🇺 Русский":
            users[user_id]["language"] = "ru"
            bot.send_message(user_id, "Привет! Рад видеть тебя здесь!  Как могу помочь?",
                             reply_markup=telebot.types.ReplyKeyboardRemove())
        elif lang == "🇬🇧 English":
            users[user_id]["language"] = "en"
            bot.send_message(user_id, "Hi there! I’m glad to see you here! \n"
                                      "Let’s get started – what can I help you with today?",
                             reply_markup=telebot.types.ReplyKeyboardRemove())
        else:
            bot.send_message(user_id, "")

        bot.send_message(OWNER_ID,
                         f"🔔 Yangi foydalanuvchi kirdi: @{users[user_id]['username']} (ID: {user_id}), til: {users[user_id]['language']}")


@bot.message_handler(content_types=message_types)
def all_message_handler(message: Message):
    if message.from_user.id == OWNER_ID:
        try:
            message_id = message.reply_to_message.message_id


            user_id = db.get_message(message_id)

            if message.content_type == "text":
                bot.send_message(user_id, message.text)
            elif message.content_type == "video":
                bot.send_video(user_id, message.video.file_id)
            elif message.content_type == "document":
                bot.send_document(user_id, message.document.file_id)
            elif message.content_type == "voice":
                bot.send_voice(user_id, message.voice.file_id)
            elif message.content_type == "sticker":
                bot.send_sticker(user_id, message.sticker.file_id)
            elif message.content_type == "audio":
                bot.send_audio(user_id, message.audio.file_id)
            elif message.content_type == "video_note":
                bot.send_video_note(user_id, message.video_note.file_id)
            elif message.content_type == "photo":
                bot.send_photo(user_id, message.photo[-1].file_id)
            elif message.content_type == "animation":
                bot.send_animation(user_id, message.animation.file_id)
            else:
                print('content type not supported')
            bot.send_message(message.from_user.id, "Xabaringiz foydalanuvchiga jo'natilindi")
        except Exception as e:
            print(e)
    else:
        db.add_message_id(message.message_id + 1, message.from_user.id)
        bot.forward_message(OWNER_ID, message.chat.id, message.message_id)
        bot.send_message(message.from_user.id,"Xabariz jo'natilindi")


bot.polling(none_stop=True)