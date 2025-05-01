import asyncio
from telegram.ext import Application, CommandHandler
from handlers.play import play
from handlers.control import add_to_queue, get_queue, get_current_track
from handlers.control import pause_command, resume_command, skip_command, stop_command
from handlers.seek import seek_command, seekback_command
from config import BOT_TOKEN

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

if __name__ == "__main__":
    asyncio.run(main())
  
