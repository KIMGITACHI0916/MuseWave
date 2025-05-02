import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from handlers.play import play
from handlers.control import add_to_queue, get_queue, get_current_track
from handlers.control import pause, resume, skip, stop
from config import BOT_TOKEN
from bot.assistants import assistant  # adjust path if needed
from pyrogram import idle
from vc import join_vc, leave_vc

async def main():
    await app.start()        # start your main bot
    await assistant.start()  # start your assistant account
    print("Bot and Assistant started!")
    await idle()
    
async def seek(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Seek functionality is not implemented yet.")

async def seekback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Seeking backward...")

async def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("play", play_audio))
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

# Entry point
if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(run_bot())
        loop.run_forever()
    except KeyboardInterrupt:
        print("Bot stopped by user.")
    
