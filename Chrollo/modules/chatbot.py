import html
import json
import re
from time import sleep

import requests
from telegram import (
    CallbackQuery,
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
    User,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.utils.helpers import mention_html

import Chrollo.modules.sql.chatbot_sql as sql
from Chrollo import BOT_ID, BOT_NAME, BOT_USERNAME, dispatcher
from Chrollo.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from Chrollo.modules.log_channel import gloggable


@user_admin_no_reply
@gloggable
def chrollorm(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"rm_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_chrollo = sql.set_chrollo(chat.id)
        if is_chrollo:
            is_chrollo = sql.set_chrollo(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"AI_DISABLED\n"
                f"<b>Admin :</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "{} Chatbot disabled by {}.".format(
                    dispatcher.bot.first_name, mention_html(user.id, user.first_name)
                ),
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin_no_reply
@gloggable
def chrolloadd(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"add_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_chrollo = sql.rem_chrollo(chat.id)
        if is_chrollo:
            is_chrollo = sql.rem_chrollo(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"AI_ENABLE\n"
                f"<b>Admin :</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "{} Chatbot enabled by {}.".format(
                    dispatcher.bot.first_name, mention_html(user.id, user.first_name)
                ),
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin
@gloggable
def chrollo(update: Update, context: CallbackContext):
    message = update.effective_message
    msg = "• Choose an option to enable/disble chatbot"
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Enable", callback_data="add_chat({})"),
                InlineKeyboardButton(text="Disable", callback_data="rm_chat({})"),
            ],
        ]
    )
    message.reply_text(
        text=msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


def chrollo_message(context: CallbackContext, message):
    reply_message = message.reply_to_message
    if message.text.lower() == "chrollo":
        return True
    elif BOT_USERNAME in message.text:
        return True
    elif reply_message:
        if reply_message.from_user.id == BOT_ID:
            return True
    else:
        return False


def chatbot(update: Update, context: CallbackContext):
    message = update.effective_message
    chat_id = update.effective_chat.id
    bot = context.bot
    is_chrollo = sql.is_chrollo(chat_id)
    if is_chrollo:
        return

    if message.text and not message.document:
        if not chrollo_message(context, message):
            return
        bot.send_chat_action(chat_id, action="typing")
        request = requests.get(
            f"https://kora-api.vercel.app/chatbot/2d94e37d-937f-4d28-9196-bd5552cac68b/{BOT_NAME}/Anonymous/message={message.text}"
        )
        results = json.loads(request.text)
        sleep(0.5)
        message.reply_text(results["reply"])


__help__ = """
*Chrollo* has a chatbot that you can engage in conversations with

 »  /chatbot *:* Shows chatbot control panel

**This feature is disabled right now due to being under development**
"""

__mod_name__ = "Chatbot"


CHATBOTK_HANDLER = CommandHandler("chatbot", chrollo, run_async=True)
ADD_CHAT_HANDLER = CallbackQueryHandler(chrolloadd, pattern=r"add_chat", run_async=True)
RM_CHAT_HANDLER = CallbackQueryHandler(chrollorm, pattern=r"rm_chat", run_async=True)
CHATBOT_HANDLER = MessageHandler(
    Filters.text
    & (~Filters.regex(r"^#[^\s]+") & ~Filters.regex(r"^!") & ~Filters.regex(r"^\/")),
    chatbot,
    run_async=True,
)

dispatcher.add_handler(ADD_CHAT_HANDLER)
dispatcher.add_handler(CHATBOTK_HANDLER)
dispatcher.add_handler(RM_CHAT_HANDLER)
dispatcher.add_handler(CHATBOT_HANDLER)

__handlers__ = [
    ADD_CHAT_HANDLER,
    CHATBOTK_HANDLER,
    RM_CHAT_HANDLER,
    CHATBOT_HANDLER,
]
