from cgitb import text
import telebot
import random
from gtts import gTTS
import qrcode



bot = telebot.TeleBot("5381538057:AAFKRdHx6MT-k_YfN4XjqGzOKpkcHL3M8u8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"سلام به بات ما خوش اومدی، میتونم اسمت رو بپرسم؟")


@bot.message_handler(func=lambda m: True)
def dd(message):
	bot.reply_to(message, message.text + "\r خوش آمدی")


@bot.message_handler(commands=['help'])
def show_menu(message):
    bot.reply_to(message,"""
/start : پیام خوش آمد
/help : توضیحات فرآیند ربات
/game ---> بازی حدس عدد را بازی کنیم
/age ---> مشاهده سن 
/voice ---> تبدیل متن انگلیسی به صدا 
/max ---> بزرگترین عدد در آرایه 
/argmax ---> اندیس بزرگترین عدد در آرایه
/qrcode ---> یه متن وارد کنید و کیو آر کد آن را بردارید """)


@bot.message_handler(commands =['voice'])
def send_m(message):
    bot.reply_to(message,"Enter your text in English")
    @bot.message_handler(func= lambda m: True)
    def teype(message):		
        myobj = gTTS(text = message.text, slow=False)
        myobj.save('file.mp3')
        voice = open('file.mp3', 'rb')
        bot.send_voice(message.chat.id, voice)


@bot.message_handler(commands=['qrcode'])
def creat_qr(message):
    bot.send_message(message.chat.id, 'Enter text ')
    @bot.message_handler(content_types=['text'])
    def creat_qr(message):
        qrcode_image =  qrcode.make("message.text")
        qrcode_image.save('qrcode.png.png')
        photo = open('qrcode.png.png','rb')
        bot.send_photo(message.chat.id, photo)



   

bot.infinity_polling()



