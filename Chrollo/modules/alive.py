from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from Chrollo import ALIVE_IMG, ALIVE_MSG, BOT_USERNAME, SUPPORT_CHAT, app

alive_button = [
    [
        InlineKeyboardButton("Help", url=f"https://t.me/{BOT_USERNAME}?start=help"),
        InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
]

@app.on_message(filters.command("alive"))
async def alive(_, message: Message):
    await message.reply_photo(
        ALIVE_IMG,
        caption=ALIVE_MSG.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(alive_button),
    )

__mod_name__ = "Alive"
