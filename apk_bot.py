from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
APK_PATH = "SVO-ZANASHIX.apk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Загрузить СВОNEWS", callback_data="get_apk")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Это приложение со списками погибших, новостями, сводками и другими материалами.",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    try:
        with open(APK_PATH, "rb") as file:
            await query.message.reply_document(
                document=file,
                filename="SVO-ZANASHIX.apk",
                caption="Если не загружается — напишите @svo_news_new"
            )
    except FileNotFoundError:
        await query.message.reply_text("Файл не найден на сервере.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()
