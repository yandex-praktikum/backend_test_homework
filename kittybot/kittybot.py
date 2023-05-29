# kittybot/kittybot.py

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

updater = Updater(token='6193616106:AAGyXs34o-7iR1uuqdv3FFrc5OgCfWtW_j0')


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def wake_up(update, context):
    # В ответ на команду /start 
    # будет отправлено сообщение 'Спасибо, что включили меня'
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Спасибо, что включили меня')


updater.dispatcher.add_handler(CommandHandler('start', wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling()
updater.idle()
