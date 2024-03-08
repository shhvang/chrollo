from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver

from Chrollo import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, SUPPORT_CHAT, pbot


@pbot.on_message(filters.command("alive"))
async def awake(_, message: Message):
   
   
    BUTTON = [
        [
            InlineKeyboardButton("Help", url=f"https://t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT_CHAT}"),
        ],
    ]

    await message.reply_photo(
        photo="https://telegra.ph/file/26ef5a0b523c9a52977ad.jpg",
        caption= """
I am alive and working perfectly fine ☄️
Refer to Support if any issue occurs
""",
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )


__mod_name__ = "Alive"
