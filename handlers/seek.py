# seek.py

from telegram import Update
from telegram.ext import ContextTypes
from player import seek_to_position, get_current_track_duration, get_playback_position

# Seek duration in seconds
DEFAULT_SEEK_AMOUNT = 10

async def seek_forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    seek_amount = DEFAULT_SEEK_AMOUNT
    if context.args:
        try:
            seek_amount = int(context.args[0])
        except ValueError:
            await update.message.reply_text("Invalid number of seconds.")
            return

    current_position = get_playback_position()
    duration = get_current_track_duration()

    if duration and current_position is not None:
        new_position = min(current_position + seek_amount, duration)
        await seek_to_position(new_position)
        await update.message.reply_text(f"Seeked forward to {new_position}s.")
    else:
        await update.message.reply_text("No track is currently playing.")


async def seek_backward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    seek_amount = DEFAULT_SEEK_AMOUNT
    if context.args:
        try:
            seek_amount = int(context.args[0])
        except ValueError:
            await update.message.reply_text("Invalid number of seconds.")
            return

    current_position = get_playback_position()
    if current_position is not None:
        new_position = max(current_position - seek_amount, 0)
        await seek_to_position(new_position)
        await update.message.reply_text(f"Seeked backward to {new_position}s.")
    else:
        await update.message.reply_text("No track is currently playing.")
      
