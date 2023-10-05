import telebot
import webbrowser
from telebot import types
import sqlite3





#bots token
bot = telebot.TeleBot('6452152757:AAEE-P-AbVgsGr5yh5nXqJt7hIJtJRShAV0')


#bu yerda pastki menyuni yaratish
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Saytga o'tish")
    markup.row(btn1)
    btn2 = types.KeyboardButton("Rasimni o'chirish")
    btn3 = types.KeyboardButton("Matinni o'zgartirish")
    markup.row(btn2, btn3)

    #file = open('start bosilganda chqadigan rasmga link', 'rb')
    #bot.send_photo(message.chat_id, file, reply_markup=markup)
    #bot.send_audio(message.chat_id, file, reply_markup=mark)

    bot.send_message(message.chat.id, f'Assalom Alekum, {message.from_user.first_name} {message.from_user.last_name} Easy Englishga Hush Kelibsiz!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


#Bu yerda tepada ko'rsatilganknopkalarga funksyalar beriladi
def on_click(message):
    if message.text == "Saytga o'tish":
        bot.send_message(message.chat.id, "Saytga o'tish uchun [bu havolaga bosing](https://example.com)")
    elif message.text == "Rasimni o'chirish":
        bot.send_message(message.chat.id, "Rasim O'chirildi!")



#userdan kelgan textdan boshqa contentlarga javob berish uchun
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    #buttonlarni designini o'zgartirish va joylashtirish
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Google ni ochish', url='https://google.com/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Rasimni o'chirish", callback_data='delete')
    markup.row(btn2)
    bot.reply_to(message, 'Ajoyib surat', reply_markup=markup)



#bu yerga websitega link berish mumkin
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.google.com')




#start button uchun
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Assalom Alekum, {message.from_user.first_name} {message.from_user.last_name} Easy Englishga Hush Kelibsiz!')


#help button uchun
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "Buyruqlar ro'yhati: ")


#slashsiz komandalar berilganda
@bot.message_handler()
def info(message):
    if message.text.lower() == 'salom':
        bot.send_message(message.chat.id,
                         f'Assalom Alekum, {message.from_user.first_name} {message.from_user.last_name} Easy Englishga Hush Kelibsiz!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f"ID: {message.from_user.id}")



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)





bot.polling(none_stop=True)