import requests

from config import BOT_TOKEN

EMOJI_IDS = {
    "🤝": 5436203513149404753,
    "🔒": 5296369303661067030,
    "💭": 5456623351042694411,
    "🚀": 6206502964224335803,
    "✔️": 6111688348529594995,
    "❤️": 5337080053119336309,
    "👑": 6203801537169334373,
}

def replace_emojis(text):
    for emoji, eid in EMOJI_IDS.items():
        text = text.replace(
            emoji,
            f'<tg-emoji emoji-id="{eid}">{emoji}</tg-emoji>'
        )
    return text

def send_message(chat_id, text, buttons=None):
    text = replace_emojis(text)

    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }

    if buttons:
        import json
        data["reply_markup"] = json.dumps({
            "inline_keyboard": buttons
        })

    resp = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json=data,
        timeout=15
    )

    print("\n===== BOT API RESPONSE =====")
    print(resp.text)
    print("============================\n")

    return resp.json()
