# control.py

from telegram import Update
from telegram.ext import ContextTypes

# In-memory queue and state (for demo purposes)
music_queue = []
is_playing = False
current_track = None


async def pause(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global is_playing
    if is_playing:
        is_playing = False
        await update.message.reply_text("Playback paused.")
    else:
        await update.message.reply_text("Nothing is playing.")


async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global is_playing
    if not is_playing and current_track:
        is_playing = True
        await update.message.reply_text("Playback resumed.")
    else:
        await update.message.reply_text("Nothing to resume.")


async def skip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_track
    if music_queue:
        current_track = music_queue.pop(0)
        await update.message.reply_text(f"Skipped. Now playing: {current_track}")
    else:
        current_track = None
    if update.message:
    await update.message.reply_text("Queue is empty.")
else:
    await update.effective_chat.send_message("Queue is empty.")


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global music_queue, is_playing, current_track
    music_queue = []
    is_playing = False
    current_track = None
    await update.message.reply_text("Playback stopped and queue cleared.")


def get_queue():
    return music_queue


def add_to_queue(track):
    music_queue.append(track)


def get_current_track():
    return current_track
  
