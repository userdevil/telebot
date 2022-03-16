from telegram import*
from telegram.ext import*
bot = Bot("5106969742:AAGm8gb9p2Ko1EUu8IvoTMTgce_ilG3ysqo")
print(bot.get_me())

updater = Updater("5106969742:AAGm8gb9p2Ko1EUu8IvoTMTgce_ilG3ysqo")
updater = Updater("5106969742:AAGm8gb9p2Ko1EUu8IvoTMTgce_ilG3ysqo",use_context = True)
dispatcher = updater.dispatcher
def test(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text = "https://g.dev/mavinsandeep")
start_value = CommandHandler('mavin',test)
dispatcher.add_handler(start_value)

def test1(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text = "https://youtube.com/channel/UCQNhxVSj8xYB0PG94UlFDJA")
start_value1 = CommandHandler('youtube',test1)
dispatcher.add_handler(start_value1)
updater.start_polling()
