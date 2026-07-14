from telethon import events, Button

from botapi import send_message
from config import (
    INTRO_VIDEO,
    WELCOME_TEXT,
    BANNED_TEXT,
    MAIN_CHANNEL,
    SETUP_CHANNEL,
    FEEDBACK_CHANNEL,
    SECOND_CHANNEL,
)

from database import (
    add_user,
    is_banned,
    is_first_start,
    disable_first_start
)

BUTTONS = [
    [
        Button.url("➜ Main Channel", MAIN_CHANNEL),
        Button.url("⚡ Setup", SETUP_CHANNEL)
    ],
    [
        Button.url("✦ Feedback", FEEDBACK_CHANNEL),
        Button.url("⬢ Updates", SECOND_CHANNEL)
    ]
]


def register(client):

    @client.on(events.NewMessage(pattern="/start"))
    async def start(event):

        sender = await event.get_sender()

        await add_user(sender)

        if await is_banned(sender.id):
            return await event.reply(
                BANNED_TEXT,
                parse_mode="html"
            )

        try:
            await client.send_file(
                event.chat_id,
                INTRO_VIDEO,
                caption="<tg-emoji emoji-id='5375464961822695044'>🎬</tg-emoji> <b>WELCOME TO BAHMAN RELAY BOT</b> <tg-emoji emoji-id='5375464961822695044'>🎬</tg-emoji>",
                    parse_mode="html"
            )
        except Exception as e:
            print("VIDEO ERROR:", e)

        send_message(
            event.chat_id,
            WELCOME_TEXT,
            [
                [
                    {"text":"➜ Main Channel","url":MAIN_CHANNEL},
                    {"text":"⚡ Setup","url":SETUP_CHANNEL}
                ],
                [
                    {"text":"✦ Feedback","url":FEEDBACK_CHANNEL},
                    {"text":"⬢ Updates","url":SECOND_CHANNEL}
                ]
            ]
        )
