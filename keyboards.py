from telethon import Button
from config import (
    MAIN_CHANNEL,
    SETUP_CHANNEL,
    FEEDBACK_CHANNEL,
    SECOND_CHANNEL
)

# =========================
# Recommended Channels
# =========================

CHANNEL_BUTTONS = [

    [
        Button.url("📢 Main", MAIN_CHANNEL),
        Button.url("⚙️ Setup", SETUP_CHANNEL)
    ],

    [
        Button.url("💬 Feedback", FEEDBACK_CHANNEL),
        Button.url("📦 Second", SECOND_CHANNEL)
    ]

]

# =========================
# Admin Panel
# =========================

ADMIN_BUTTONS = [

    [
        Button.inline("📊 Stats", b"stats"),
        Button.inline("📢 Broadcast", b"broadcast")
    ],

    [
        Button.inline("🚫 Ban", b"ban"),
        Button.inline("✅ Unban", b"unban")
    ]

]

# =========================
# Back Button
# =========================

BACK_BUTTON = [
    [
        Button.inline("⬅ Back", b"back")
    ]
]
