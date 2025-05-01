import asyncio
from telegram.ext import Application, CommandHandler
from handlers.play import play_command
from handlers.control import add_to_queue, get_queue, get_current_track
from handlers.control import pause_command, resume_command, skip_command, stop_command
from handlers.seek import seek_command, seekback_command
from config import BOT_TOKEN

async def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("play", play_command))
    application.add_handler(CommandHandler("pause", pause_command))
    application.add_handler(CommandHandler("resume", resume_command))
    application.add_handler(CommandHandler("skip", skip_command))
    application.add_handler(CommandHandler("stop", stop_command))
    application.add_handler(CommandHandler("seek", seek_command))
    application.add_handler(CommandHandler("seekback", seekback_command))

    print("Music bot is running...")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
  
