from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "حط التوكن هنا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا بيك 👋")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
