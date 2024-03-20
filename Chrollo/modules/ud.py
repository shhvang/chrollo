import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from Chrollo import dispatcher
from Chrollo.modules.disable import DisableAbleCommandHandler


def ud(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text[len("/ud "):]
    results = requests.get(f"https://api.urbandictionary.com/v0/define?term={text}").json()
    
    try:
        if results["list"]:
            reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
        else:
            reply_text = "No definitions found for that term."
    except Exception as e:
          # Print the exception for debugging purposes
        reply_text = f"An error occurred while fetching the definition. {e}"
    
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)

def define(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text[len("/define ") :]
    results = requests.get(
        f"https://api.dictionaryapi.dev/api/v2/entries/en/{text}"
    ).json()
    try:
        reply_text = f'*{text}*\n\n{results["definition"]}_'
    except:
        reply_text = "No results found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


UD_HANDLER = DisableAbleCommandHandler(["ud"], ud, run_async=True)
DEFINE_HANDLER = DisableAbleCommandHandler(["define"], define, run_async=True)

dispatcher.add_handler(DEFINE_HANDLER)
dispatcher.add_handler(UD_HANDLER)

__help__ = """
» /ud (text) *:* Gives off a randomly written shitty definition
» /define (text) *:* The actual dictionary 
"""
__mod_name__ = "Define"

__command_list__ = ["ud"], ["define"]
__handlers__ = [UD_HANDLER], [DEFINE_HANDLER]
