from telegram import*
from datetime import datetime
from telegram.ext import*
import telebot

bot = Bot("5106969742:AAGm8gb9p2Ko1EUu8IvoTMTgce_ilG3ysqo")
print(bot.get_me())

TOKEN = '5106969742:AAGm8gb9p2Ko1EUu8IvoTMTgce_ilG3ysqo'
bt = telebot.TeleBot(TOKEN)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def test_send_message():
        text = 'CI Test Message'
        tb = telebot.TeleBot(TOKEN)
        ret_msg = tb.send_message(CHAT_ID, text)
        assert ret_msg.message_id

if current_time=='24:00:00':
    test_send_message()

updater = Updater("5106969742:AAGm8gb9p2Ko1EUu8IvoTMTgce_ilG3ysqo")
updater = Updater("5106969742:AAGm8gb9p2Ko1EUu8IvoTMTgce_ilG3ysqo",use_context = True)
dispatcher = updater.dispatcher
def test(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text = "https://g.dev/mavinsandeep")
start_value = CommandHandler('mavin',test)
dispatcher.add_handler(start_value)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /instagram - To get the Instagram profile URL
    /tutorials - To get python Tutorial URL
    /tutorialmodels - To get separate tutorials
    /API - To get developement api's developed by coding with ms
    /Website - To get the Website URL""")
  
  
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "https://codingwithms-60edd.web.app/tutorial.html")
  
  
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/channel/UCQNhxVSj8xYB0PG94UlFDJA/null")
  
  
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Instagram URL => \
        https://www.instagram.com/coding_with_ms_/")
  
  
def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Website URL => https://codingwithms-60edd.web.app/")
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
def tut(update: Update, context: CallbackContext):
    update.message.reply_text("""Available TUtorials :-
    https://www.youtube.com/channel/UCQNhxVSj8xYB0PG94UlFDJA/videos""")
   
def api(update: Update, context: CallbackContext):
    update.message.reply_text("""Available API's :-
    End Url Tracking - https://redliapi.herokuapp.com/
    Encoder - https://encapi.herokuapp.com/""")
    
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('tutorialmodels', tut))
updater.dispatcher.add_handler(CommandHandler('API', api))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('instagram', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('tutorials', gmail_url))
updater.dispatcher.add_handler(CommandHandler('Website', geeks_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.start_polling()
bt.polling()
