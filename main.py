import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from handlers.play import play
from handlers.control import add_to_queue, get_queue, get_current_track
from handlers.control import pause, resume, skip, stop
from config import BOT_TOKEN

# Extra commands
async def seek(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Seek functionality is not implemented yet.")

async def seekback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Seeking backward...")

# Main async function
async def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("play", play))
    application.add_handler(CommandHandler("pause", pause))
    application.add_handler(CommandHandler("resume", resume))
    application.add_handler(CommandHandler("skip", skip))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("seek", seek))
    application.add_handler(CommandHandler("seekback", seekback))

    print("Music bot is running...")
    await application.run_polling()

# Entry point
if __name__ == "__main__":
    import asyncio

    try:
        loop = asyncio.get_event_loop()
        loop.create_task(main())
        loop.run_forever()
    except KeyboardInterrupt:
        print("Bot stopped by user.")
