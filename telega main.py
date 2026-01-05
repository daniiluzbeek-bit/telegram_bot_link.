import telebot

bot = telebot.TeleBot("8242338904:AAGISs9jcFTCsK9U316DlzFVyCOl-rF8gF4")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello=напиши /help что бы узнать подробно')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Привет это бот для скачивания видео из тик тока напиши /Main что бы звязатся с разработчиком это 1 версия она не работает!')

@bot.message_handler(commands=['Main'])
def Main(message):
    bot.send_message(message.chat.id, '@Daanil2417 не спамить!!_а еще есть функция узнать информацию об этом чате и пользователь(Докс) напишите команду /hello')

@bot.message_handler(commands=['hello'])
def show_hello_info(message):
    text = (
        f"User ID: {message.from_user.id}\n"
        f"Username: @{message.from_user.username}\n"
        f"First name: {message.from_user.first_name}\n"
        f"Chat ID: {message.chat.id}\n"
        f"Chat type: {message.chat.type}\n"
        f"Text: {message.text}"
    )

    bot.send_message(message.chat.id, text)

bot.infinity_polling(none_stop=True)
