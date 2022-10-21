#from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler #, CallbackContext
from tictactoe import *


updater = Updater('5626334014:AAF-W-CnZbhM-UXlyRF-KTKnfzSha2zpR0I')
"""updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))"""
updater.dispatcher.add_handler(CommandHandler('start', newGame))

updater.dispatcher.add_handler(CallbackQueryHandler(button))
print('server start')
updater.start_polling()
updater.idle()