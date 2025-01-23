import telebot
import pickle
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message

API_TOKEN = "7785376105:AAEPeFWk6Vm7RrVdjf1Bjxrbd3IIleiYY_g"
OWNER_ID = 8091838884

bot = telebot.TeleBot(API_TOKEN)

users = {}

message_types = ["text", "video", "document", "voice", "audio", "sticker", "video_note"]

class MessagesDb:
    db_path = './telegram.db'

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
        print('keldi')
        print(self.message_ids)
        # print(self.message_ids[message_id], self.message_ids)
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


# @bot.message_handler(func=lambda message: message.from_user.id != OWNER_ID)
# def forward_to_owner(message):
#     user_id = message.from_user.id
#     username = users.get(user_id, {}).get("username", f"User_{user_id}")
#
#     bot.send_message(OWNER_ID, f"📩 Yangi xabar @{username} (ID: {user_id}) dan:\n\n{message.text}")
#     bot.send_message(user_id, "✅ Xabaringiz jo‘natildi.")
#
#
# @bot.message_handler(func=lambda message: message.from_user.id == OWNER_ID and message.reply_to_message)
# def reply_to_user(message):
#     text = message.text
#     reply_text = message.reply_to_message.text
#
#     for user_id, user_data in users.items():
#         if f"@{user_data['username']}" in reply_text or f"(ID: {user_id})" in reply_text:
#             bot.send_message(user_id, f"📩 Yangi xabar: {text}")
#             bot.send_message(OWNER_ID, "✅ Xabaringiz foydalanuvchiga jo‘natildi.")
#             return
#
#     bot.send_message(OWNER_ID, "❌ Foydalanuvchini aniqlab bo‘lmadi.")

# @bot.message_handler(content_types=message_types)
# def forward_to_owner(message):
#     """Foydalanuvchi xabarlarini adminga yuboradi."""
#     if message.from_user.id != OWNER_ID:
#         print('asd')
#
#         user_id = message.from_user.id
#         username = users.get(user_id, {}).get("username", f"User_{user_id}")
#
#         # Adminga foydalanuvchi haqida ma'lumot yuborish
#         bot.send_message(OWNER_ID, f"📩 Yangi xabar @{username} (ID: {user_id}):")
#
#         # Xabar turiga qarab jo‘natish
#         if message.text:
#             bot.send_message(OWNER_ID, message.text)
#         elif message.photo:
#             bot.send_photo(OWNER_ID, message.photo[-1].file_id, caption=message.caption if message.caption else None)
#         elif message.sticker:
#             bot.send_sticker(OWNER_ID, message.sticker.file_id)
#         elif message.video:
#             bot.send_video(OWNER_ID, message.video.file_id, caption=message.caption if message.caption else None)
#         elif message.document:
#             bot.send_document(OWNER_ID, message.document.file_id)
#         elif message.voice:
#             bot.send_voice(OWNER_ID, message.voice.file_id)
#         elif message.audio:
#             bot.send_audio(OWNER_ID, message.audio.file_id)
#
#         bot.send_message(user_id, "✅ Xabaringiz jo‘natildi.")
#
#
# @bot.message_handler(content_types=message_types)
# def forward_to_owner(message: Message):
#     if message.from_user.id == OWNER_ID:
#         try:
#             chat_id = int(message.reply_to_message.text.split("$@$")[0])
#
#             if message.text:
#                 bot.send_message(chat_id,"Xabaringiz jo'natilindi!")
#                 bot.forward_message(chat_id, message.text,message.from_user.id)
#             if message.sticker:
#                 bot.send_message(chat_id,message.sticker.file_id,message.)
#         except Exception as e:
#             print(e)
#     else:
#         print(message.text)
#         user_id_text = f'{message.from_user.id}$@${message.from_user.first_name}\n'
#         if message.text:
#             text = user_id_text + message.text
#             bot.send_message(OWNER_ID, text)
#             bot.send_message(OWNER_ID, "Xabaringiz jo'natilindi!!!")
#         if message.sticker:
#             bot.send_sticker(OWNER_ID, message.sticker)
#             bot.forward_message(OWNER_ID, user_id_text + 'sticker',message.from_user.id)


    # if message.from_user.id == OWNER_ID:
    #     try:
    #         chat_id = message.reply_to_message.forward_from.id
    #         if message.text:
    #             bot.send_message(chat_id, message.text)
    #         elif message.video:
    #             bot.send_video(chat_id, message.video)
    #         elif message.document:
    #             bot.send_document(chat_id, message.document)
    #             print('asd')
    #     except Exception as e:
    #         print(e)
    # else:
    #     try:
    #         print('client')
    #     except Exception as e:
    #         print(e)

    # user_id = message.from_user.id
    # username = users.get(user_id, {}).get("username", f"User_{user_id}")
    #
    # # Adminga foydalanuvchi haqida ma'lumot yuborish
    # bot.send_message(OWNER_ID, f"📩 Yangi xabar @{username} (ID: {user_id}):")
    #
    # # Xabar turiga qarab jo‘natish
    # if message.text:
    #     bot.send_message(OWNER_ID, message.text)
    # elif message.photo:
    #     bot.send_photo(OWNER_ID, message.photo[-1].file_id, caption=message.caption if message.caption else None)
    # elif message.sticker:
    #     bot.send_sticker(OWNER_ID, message.sticker.file_id)
    # elif message.video:
    #     bot.send_video(OWNER_ID, message.video.file_id, caption=message.caption if message.caption else None)
    # elif message.document:
    #     bot.send_document(OWNER_ID, message.document.file_id)
    # elif message.voice:
    #     bot.send_voice(OWNER_ID, message.voice.file_id)
    # elif message.audio:
    #     bot.send_audio(OWNER_ID, message.audio.file_id)
    #
    # bot.send_message(user_id, "✅ Xabaringiz jo‘natildi.")


#
# # func=lambda message: message.from_user.id == OWNER_ID and message.reply_to_message
# @bot.message_handler(content_types=message_types)
# def reply_to_user(message):
#     """Admin foydalanuvchiga javob yozganda, xabar to‘g‘ri odamga boradi."""
#     original_message = message.reply_to_message  # Admin reply qilgan xabar
#     user_id = original_message.forward_from.id if original_message.forward_from else None
#
#     # Agar forward_from mavjud bo‘lmasa, username yoki ID orqali aniqlash
#     if not user_id:
#         for uid, user_data in users.items():
#             if original_message.text and (
#                     f"@{user_data['username']}" in original_message.text or f"(ID: {uid})" in original_message.text):
#                 user_id = uid
#                 break
#
#     if not user_id:
#         bot.send_message(OWNER_ID, "❌ Foydalanuvchini aniqlab bo‘lmadi.")
#         return
#
#     # Admin javobini foydalanuvchiga jo‘natish
#     if message.text:
#         bot.send_message(user_id, f"📩 Admindan javob:\n\n{message.text}")
#     elif message.photo:
#         bot.send_photo(user_id, message.photo[-1].file_id, caption=message.caption if message.caption else None)
#     elif message.sticker:
#         bot.send_sticker(user_id, message.sticker.file_id)
#     elif message.video:
#         bot.send_video(user_id, message.video.file_id, caption=message.caption if message.caption else None)
#     elif message.document:
#         bot.send_document(user_id, message.document.file_id)
#     elif message.voice:
#         bot.send_voice(user_id, message.voice.file_id)
#     elif message.audio:
#         bot.send_audio(user_id, message.audio.file_id)
#     else:
#         bot.send_message(OWNER_ID, "❌ Ushbu xabar turini foydalanuvchiga yubora olmayman.")
#
#     bot.send_message(OWNER_ID, f"✅ Xabaringiz foydalanuvchiga (ID: {user_id}) jo‘natildi.")



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
                print(message)
                bot.send_sticker(user_id, message.sticker.file_id)
            elif message.content_type == "audio":
                bot.send_audio(user_id, message.audio.file_id)
            elif message.content_type == "video_note":
                bot.send_video_note(user_id, message.video_note.file_id)
            else:
                print('content type not supported')
        except Exception as e:
            print(e)
    else:
        db.add_message_id(message.message_id + 1, message.from_user.id)
        bot.forward_message(OWNER_ID, message.chat.id, message.message_id)


bot.polling(none_stop=True)
