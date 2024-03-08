from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as o
from telethon import __version__ as s

from Chrollo import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, pbot


@pbot.on_message(filters.command(["repo", "source"]))
async def repo(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption="I am Chrollo from Hunter x Hunter",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Developer", user_id=OWNER_ID),
                    InlineKeyboardButton(
                        "Source",
                        url="https://youtu.be/dQw4w9WgXcQ?si=MbU0BmZfBNYwwXe3",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Repo"
