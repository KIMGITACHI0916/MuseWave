from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.stream import AudioPiped  # Note: old version uses "input_streams"
from pyrogram import Client
from config import API_ID, API_HASH, SESSION_STRING

client = Client("music", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
pytgcalls = PyTgCalls(client)

async def join_vc(chat_id: int, audio_file: str):
    await pytgcalls.join_group_call(
        chat_id,
        AudioPiped(audio_file),
    )

async def leave_vc(chat_id: int):
    await pytgcalls.leave_group_call(chat_id)
