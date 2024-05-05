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

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def define_word(update, context):
  """Responds to /define commands with word definitions."""
  chat_id = update.effective_message.chat_id
  word = update.effective_message.text.split()[1]  # Extract word after "/define"

  try:
    response = requests.get(f"{API_URL}{word}")
    response.raise_for_status()  # Raise exception for non-200 status codes

    # Parse JSON response (adjust key names based on specific API)
    data = response.json()[0]
    definition = data["meanings"][0]["definitions"][0]["definition"]
    try:
        example = data["meanings"][0]["definitions"][0]["example"]
    except KeyError:
        example = "No example found for this word."  # Set a default value or message
    try:
        synonyms = ", ".join([synonym["sense"] for synonym in data["synonyms"]])
    except KeyError:
        synonyms = "No synonyms found."

    # Build response message
    message = f"**Definition of {word.title()}**\n\n{definition}\n\n**Example:**\n{example}\n\n**Synonyms:**\n{synonyms}"
    update.message.reply_text(message, parse_mode="Markdown")

  except requests.exceptions.RequestException as e:
    update.message.reply_text(f"An error occurred: {e}")
  except IndexError:  # Handle cases where word not found in API response
    update.message.reply_text(f"Sorry, couldn't find a definition for '{word}'.")


UD_HANDLER = DisableAbleCommandHandler(["ud"], ud, run_async=True)
DEFINE_HANDLER = DisableAbleCommandHandler(["define"], define_word, run_async=True)

dispatcher.add_handler(DEFINE_HANDLER)
dispatcher.add_handler(UD_HANDLER)

__help__ = """
» /ud (text) *:* Gives off a randomly written shitty definition
» /define (text) *:* The actual dictionary 
"""
__mod_name__ = "Define"

__command_list__ = ["ud"], ["define"]
__handlers__ = [UD_HANDLER], [DEFINE_HANDLER]
