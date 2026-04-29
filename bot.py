from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "حط التوكن هنا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا 👋 البوت شغال 24/7")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
