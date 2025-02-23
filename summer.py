from telegram import Update ,ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext,MessageHandler,filters ,ConversationHandler
from summerfc import *

TOKEN = "" #token for telegram bot


api_key = ""  # key for gimine



async def start(update: Update, context: CallbackContext) -> None:
    #await update.message.reply_text("Hello")
    await update.message.reply_text("write you want summer")

async def summerai(update: Update, context: CallbackContext) -> None:
    #if update.message.text == 'Option 2':
    #await update.message.reply_text('ok')
    
    article_text = update.message.text
    summary = summarize_article(api_key, article_text, word_limit=100)
    await update.message.reply_text(summary['parts'][0]['text'])





def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, summerai))
    #app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, amine))
    print("Bot is running...")
    app.run_polling()


main()
