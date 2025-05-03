import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from handlers.play import play_audio  # FIX: use the actual function name
from handlers.control import pause, resume, skip, stop
from config import BOT_TOKEN
from bot.assistants import assistant
from pyrogram import idle
from vc import join_vc, leave_vc  # Ensure vc.py is fixed as discussed

async def seek(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Seek functionality is not implemented yet.")

async def seekback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Seeking backward...")

async def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("play", play_audio))  # FIXED
    application.add_handler(CommandHandler("pause", pause))
    application.add_handler(CommandHandler("resume", resume))
    application.add_handler(CommandHandler("skip", skip))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("seek", seek))
    application.add_handler(CommandHandler("seekback", seekback))

    print("Music bot is running...")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

async def main():
    await app.start()        # This should be `application`, not `app`
    await assistant.start()
    print("Bot and Assistant started!")
    await idle()

if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        print("Bot stopped by user.")
        
