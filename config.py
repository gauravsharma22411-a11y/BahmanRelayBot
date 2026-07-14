import os
from dotenv import load_dotenv

load_dotenv()

# ===========================
# Telegram Credentials
# ===========================

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
# ===========================
# Bot Information
# ===========================

BOT_NAME = "BAHMAN RELAY BOT"
INTRO_VIDEO = "intro.mp4"

# ===========================
# Official Channels
# ===========================

MAIN_CHANNEL = "https://telegram.me/+ZK8xSfPU5Qc0N2U1"
SETUP_CHANNEL = "https://t.me/Bahmanmodzsetup"
FEEDBACK_CHANNEL = "https://t.me/BAHMANMODZ"
SECOND_CHANNEL = "https://telegram.me/CRIMSONFUNERAL16"

# ===========================
# Premium Emoji IDs
# ===========================

EMOJIS = {
    "welcome": "6203801537169334373",
    "loading": "5386367538735104399",
    "lightning": "6251159113590382030",
    "lock": "5296369303661067030",
    "shield": "5296369303661067030",
    "rocket": "6206502964224335803",
    "message": "5456623351042694411",
    "send": "5368554037320900698",
    "success": "6111688348529594995",
    "error": "6206129418033700314",
    "warning": "6206405305257959272",
    "heart": "6206517713142031259",
    "main": "5769482310915199790",
    "setup": "5341715473882955310",
    "feedback": "5332554596403404883",
    "second": "5355193051193059834",
    "user": "5258011929993026890",
    "owner": "5814534640949530526",
    "home": "5416041192905265756",
    "stats": "5231200819986047254",
    "help": "6203826834526707259",
    "back": "5852777596688797905",
    "add": "5305329417189340362",
    "remove": "5346289768672020876",
    "refresh": "5244758760429213978",
}


def e(name: str):
    """
    Returns Telegram Premium custom emoji HTML.
    """
    return f'<tg-emoji emoji-id="{EMOJIS[name]}">⭐</tg-emoji>'

WELCOME_TEXT = f"""
<tg-emoji emoji-id='6061949981542059119'>👻</tg-emoji><tg-emoji emoji-id='6064591175975701283'>😇</tg-emoji><tg-emoji emoji-id='6061980810817309486'>🥰</tg-emoji><tg-emoji emoji-id='6064273361280699223'>😘</tg-emoji><tg-emoji emoji-id='6061938410900163529'>💩</tg-emoji><tg-emoji emoji-id='6062263196327086241'>✍️</tg-emoji><tg-emoji emoji-id='6062098810748800030'>🍡</tg-emoji><tg-emoji emoji-id='6062126732331191028'>🎈</tg-emoji>

<tg-emoji emoji-id="5296369303661067030">🔒</tg-emoji> <b>SECURE ANONYMOUS RELAY</b> <tg-emoji emoji-id="5296369303661067030">🔒</tg-emoji>

<tg-emoji emoji-id="6204068035595083931">🛡️</tg-emoji> <b>YOUR IDENTITY STAYS PRIVATE</b> <tg-emoji emoji-id="6204068035595083931">🛡️</tg-emoji>

<tg-emoji emoji-id="5456623351042694411">💭</tg-emoji> <b>SEND ANY MESSAGE BELOW</b> <tg-emoji emoji-id="5456623351042694411">💭</tg-emoji>

<tg-emoji emoji-id="6251159113590382030">⚡</tg-emoji> <b>THE OWNER WILL REPLY HERE</b> <tg-emoji emoji-id="6251159113590382030">⚡</tg-emoji>

<tg-emoji emoji-id='6061949981542059119'>👻</tg-emoji><tg-emoji emoji-id='6064591175975701283'>😇</tg-emoji><tg-emoji emoji-id='6061980810817309486'>🥰</tg-emoji><tg-emoji emoji-id='6064273361280699223'>😘</tg-emoji><tg-emoji emoji-id='6061938410900163529'>💩</tg-emoji><tg-emoji emoji-id='6062263196327086241'>✍️</tg-emoji><tg-emoji emoji-id='6062098810748800030'>🍡</tg-emoji><tg-emoji emoji-id='6062126732331191028'>🎈</tg-emoji>
"""

DELIVERED_TEXT = f"""
{e("success")} <b>Message Delivered Successfully</b>

{e("rocket")} Please wait for the owner's reply.

<tg-emoji emoji-id='6061949981542059119'>👻</tg-emoji><tg-emoji emoji-id='6064591175975701283'>😇</tg-emoji><tg-emoji emoji-id='6061980810817309486'>🥰</tg-emoji><tg-emoji emoji-id='6064273361280699223'>😘</tg-emoji><tg-emoji emoji-id='6061938410900163529'>💩</tg-emoji><tg-emoji emoji-id='6062263196327086241'>✍️</tg-emoji><tg-emoji emoji-id='6062098810748800030'>🍡</tg-emoji><tg-emoji emoji-id='6062126732331191028'>🎈</tg-emoji>
"""

BANNED_TEXT = f"""
{e("error")} <b>You are blocked from using this bot.</b>

"""
