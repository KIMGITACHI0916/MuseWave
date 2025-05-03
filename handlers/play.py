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

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /play <song name or YouTube/Spotify link>")
        return

    query = ' '.join(context.args)

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            video = info['entries'][0] if 'entries' in info else info
            video_title = video.get("title", "audio")
            video_url = video.get("webpage_url")

        # Download audio
        file_name = f"{video_title}.mp3"
        download_opts = {
            'format': 'bestaudio',
            'outtmpl': file_name
        }
        with YoutubeDL(download_opts) as ydl:
            ydl.download([video_url])

        track = f"{video_title} ({video_url})"

        if get_current_track():
            add_to_queue(track)
            await update.message.reply_text(f"Added to queue: {track}")
        else:
            add_to_queue(track)
            await update.message.reply_text(f"Now playing: {track}")
            # You would now stream the audio file_name here

    except Exception as e:
        await update.message.reply_text(f"Error playing track: {e}")
        
