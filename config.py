import os
from pyrogram import Client
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# === Telegram Bot Token ===
BOT_TOKEN = os.getenv("BOT_TOKEN", "8137618565:AAHJZBJa4hXc1j0PFyoGHksN_G8zcLHaUMo")

# === Pyrogram Client (for voice chat streaming) ===
API_ID = int(os.getenv("API_ID", "22661093"))
API_HASH = os.getenv("API_HASH", "344d2a8926320e2cf9211f0ffda9c03a")

# Create Pyrogram client
pyro_client = Client(
    "music_bot_client",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# === Spotify API ===
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "6e4a71e7aa074b89ab562b47c87f80eb")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "e25c04bddc0e42c792df478674cd7f10")

spotify_auth_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)
spotify = spotipy.Spotify(auth_manager=spotify_auth_manager)

