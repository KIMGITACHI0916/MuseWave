from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream, AudioPiped
from pyrogram import Client
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream import InputStream  # Only if needed

# This should be your assistant Pyrogram client
from bot.assistants import assistant  # adjust the import if needed

pytgcalls = PyTgCalls(assistant)

async def join_vc(chat_id: int, audio_path: str):
    await pytgcalls.join_group_call(
        chat_id,
        InputStream(
            AudioPiped(audio_path),
        ),
    )

async def leave_vc(chat_id: int):
    await pytgcalls.leave_group_call(chat_id)
  
