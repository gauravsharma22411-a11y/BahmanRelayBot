import asyncio
from config import e

STEPS = [
    (
        f"{e('loading')} <b>Initializing secure relay...</b>\n\n"
        f"{e('shield')} Creating encrypted tunnel..."
    ),
    (
        f"{e('lightning')} <b>Encrypting your message...</b>\n\n"
        f"{e('lock')} Protecting your identity..."
    ),
    (
        f"{e('send')} <b>Delivering message...</b>\n\n"
        f"{e('rocket')} Sending to owner..."
    ),
    (
        f"{e('success')} <b>Delivered Successfully!</b>\n\n"
        f"{e('heart')} The owner will reply here when available."
    )
]


async def play(client, chat_id):
    msg = await client.send_message(
        chat_id,
        STEPS[0],
        parse_mode="html"
    )

    for step in STEPS[1:]:
        await asyncio.sleep(1)
        await msg.edit(
            step,
            parse_mode="html"
        )

    return msg
