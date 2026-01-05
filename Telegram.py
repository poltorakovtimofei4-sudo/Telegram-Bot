###
import Telebot

TOKEN = ("YOUR BOT TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.messange_handler(command=['start'])
def send_welcome(messange):
	bot.reply_to(messange, "What's your name?")

@bot.messange_handler(func=lambda messange:True)
def send_your_name(messange):
	name = messange.text.strip()
	bot.reply_to(messange, "Hello {name}!")

bot.polling()
