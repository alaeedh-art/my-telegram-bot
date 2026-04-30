from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "1406262369:AAHeO_m3HOnkCNYq-PHRooBAFIzTMipDMW0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 👋 Bot is running")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
