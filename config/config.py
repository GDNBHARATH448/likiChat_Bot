from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = " 20853237"
# -------------------------------------------------------------
API_HASH = "229d3180fe02247b931c56e355e83458"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7264011138:AAEj-MHUtfVNVcdv7tN1i0sN308QNcM7xf4")
STRING1 = getenv("STRING_SESSION", "BQE-MfUAou2PlnQ1lEYZSBBqH0qyWSS5rbvWnGECiquSFY6IaDPRxH4WGDkZRvcIYYXw1K4MFYMbjAV5YWeWjyPYa0auKT_YZT8g9NdKfcpjFxOC623Jf_qImPQQ9sZ7-VlrJu2ybwpQ3CwZAJt5heOAxyQOx_oKeoBeXr3TG-7615VL1AvK4f1Qx1rhuX68VEC_QsSmXUXN2s_2UlLBldpG34f4w8RfH-Jcvr8pPwqtoSkOOb-youkN3BzU27bi5pQQ-AYabiUZtEAMUOwDlYlDlBUYrq-RMp879dr9lUb5ah7EUcEWn_2sQLfd1enOZ6_HqJOqXJyOBsyaNptZOQIAS62nRAAAAAHnecIdAA")
DB_NAME = "shizuDB"
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Likhith:Likhithbots@likhith.jm3wayg.mongodb.net/?retryWrites=true&w=majority&appName=likhith")
OWNER_ID = int(getenv("OWNER_ID", "5867783630"))
BOT_ID = int(getenv("BOT_ID", "7264011138"))
SUPPORT_GRP = "kannada_chatting0"
UPDATE_CHNL = "dpzchannel143"
OWNER_USERNAME = "Likith812"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002889415304"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7946875913").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/GDNBHARATH448/likiChat_Bot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
