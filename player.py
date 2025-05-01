import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from yt_dlp import YoutubeDL
from telegram import Update
from telegram.ext import ContextTypes

# Initialize Spotify with environment variables
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

spotify = Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

# YT-DLP options for searching and extracting YouTube audio
ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'quiet': True,
    'default_search': 'ytsearch',
    'extract_flat': 'in_playlist',
}


async def play_spotify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /play <Spotify track link or search query>")
        return

    query = ' '.join(context.args)

    try:
        # If Spotify link
        if "open.spotify.com/track" in query:
            track_id = query.split("track/")[1].split("?")[0]
            track = spotify.track(track_id)
            track_title = f"{track['name']} - {track['artists'][0]['name']}"
        else:
            # Text search on Spotify
            results = spotify.search(q=query, type='track', limit=1)
            if not results['tracks']['items']:
                await update.message.reply_text("No Spotify track found for the query.")
                return
            track = results['tracks']['items'][0]
            track_title = f"{track['name']} - {track['artists'][0]['name']}"

        await update.message.reply_text(f"Searching YouTube for: {track_title}")

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(track_title, download=False)
            video = info['entries'][0] if 'entries' in info else info
            video_url = video['url']
            video_title = video['title']

        await update.message.reply_text(f"Playing: {video_title}\n{video_url}")

    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
