class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 25203487
    API_HASH = "97159488e0ac2293cd72bcf5a3c1a24d"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://chrollo_owner:ijp7C1KeNgEz@ep-rough-wind-a52tzt0n.us-east-2.aws.neon.tech/chrollo?sslmode=require"  # A sql database url from elephantsql.com

    EVENT_LOGS = -1001865457292  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://chrollodb:chrollodb@cluster0.fay8b9c.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/d623ac53ee21f196bd8c4.jpg"

    SUPPORT_CHAT = "IOSupportChat"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6438153237:AAHV-PslvZpbdn62izhlpgCcZAhFjvYfHOA"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID =  5552153244 # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [5552153244]  # User id of sudo users
    DEV_USERS = [6142070797]  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
