import os
from yt_dlp import YoutubeDL
from telegram import Update
from telegram.ext import ContextTypes
from handlers.control import add_to_queue, get_queue, get_current_track

# YT-DLP options to extract YouTube audio info
ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'quiet': True,
    'default_search': 'ytsearch',
    'extract_flat': 'in_playlist',
}

# Download audio file from YouTube
file_name = f"{video_title}.mp3"
with YoutubeDL({'format': 'bestaudio', 'outtmpl': file_name}) as ydl:
    ydl.download([video['webpage_url']])

async def play_audio(update, context):
    await join_vc(update.effective_chat.id, file_name)


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /play <song name or YouTube/Spotify link>")
        return

    query = ' '.join(context.args)

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            video = info['entries'][0] if 'entries' in info else info
            video_url = video['url']
            video_title = video['title']

        track = f"{video_title} ({video_url})"

        if get_current_track():
            add_to_queue(track)
            await update.message.reply_text(f"Added to queue: {track}")
        else:
            add_to_queue(track)
            await update.message.reply_text(f"Now playing: {track}")

    except Exception as e:
        await update.message.reply_text(f"Error playing track: {e}")
        
