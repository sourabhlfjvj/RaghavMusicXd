from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AarohiX import app
import string
from strings import get_command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

RAGHAV = [" **◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** \n\n🍃**Look at the stars, look how they shine for you and everything you do....**🍃 \n\n**I hope you don't mind that I put down in words how wonderful life is while you're in the world.** \n\n**◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** ",
       " **◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** \n\n🍃**🌹❝◂ 𝐈 𝐏ʀᴏᴍɪsᴇ ▸**🍃 \n\n**◂𝐘ᴏᴜ 𝐇ᴀᴠᴇ 𝐌ᴇ,𝐔ɴᴛɪʟ 𝐌ʏ 𝐋ᴀsᴛ 𝐁ʀᴇᴀᴛʜ▸❞🌹** \n\n**◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** ",
       " **◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** \n\n 🍃**Jab bhi Dekhta hu Tumhe ,Lagta hai ye Din Naya hai**🍃 \n\n**✨❤️ Nigahein Tumko Dekhna Chahti hai ,Mere Dilko ye kya hua hai♥️✨** \n\n**◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** "]

# Command of DILxAAROHI
DIL_COMMAND = get_command("DIL_COMMAND")

@app.on_message(
    filters.command(DIL_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(DIL),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👻sᴜᴩᴩᴏʀᴛ👻", url=f"https://t.me/premnagriii"),
                    InlineKeyboardButton(
                        "🫠ᴍᴀɪɴᴛᴀɪɴᴇʀ🫠", url=f"https://t.me/lll_KILL_YOU_lll")
                    
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(DIL_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(DIL),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 👻sᴜᴩᴩᴏʀᴛ 👻", url=f"https://t.me/premnagriii"),
                    InlineKeyboardButton(
                        "🫠ᴍᴀɪɴᴛᴀɪɴᴇʀ🫠", url=f"https://t.me/lll_KILL_YOU_lll")
                    
                ]
            ]
        ),
    )
