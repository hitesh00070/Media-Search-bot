import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = 4639219
API_HASH = '8aa6ff17490134bf275616030f46e29e'
BOT_TOKEN = '6031547979:AAF1Xx1Nzm_vCXCY85tYCXwsr93As1kYZaA'
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = 678710922
CHANNELS = ['-1001538461400']
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = -1001531025479

# MongoDB information
DATABASE_URI = "mongodb+srv://jns4638:jns4638@cluster0.qyh3o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = 'cinee'
COLLECTION_NAME = 'channel_files'

# Messages
default_start_msg = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @cinee_update to use this bot')
