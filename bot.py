import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8658062057:AAFWONT1PF8IYY8QY4g556aesQf_BK0xa1w")
WEBAPP_URL = os.environ.get("WEBAPP_URL", "https://classy-buttercream-21d071.netlify.app/")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name if user.first_name else "Okushy"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            text="Kursti basta 🚀🚀🚀",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])

    await update.message.reply_text(
        f"Assalaumagaleikum, {name}! 👋\n\n"
        f"Karzylyk Kaizen kursyna kosh keldiniz!\n\n"
        f"Kursti bastau ushin tomendegi batyrmany basynyzy 👇",
        reply_markup=keyboard,
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
