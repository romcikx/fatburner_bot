import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Define a function that will be triggered when the user clicks the button
def button(update, context):
    query = update.callback_query
    url = "https://n.fcd.su/P6A"
    query.answer()
    query.message.reply_text("Here's your link: " + url)

# Define a function that will be triggered when the user sends a message to the bot
def start(update, context):
    keyboard = [[InlineKeyboardButton("Get Link", callback_data='1')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Hello! Press the button to get a link.', reply_markup=reply_markup)

# Set up the bot and add the handlers
updater = Updater(token='6120148818:AAFYV3bJ-2LQcl_gcX4BR5Y18K_TGayROhw', use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()

# Run the bot
updater.idle()
