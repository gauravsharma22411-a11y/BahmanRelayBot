from telethon import events

from config import (
    OWNER_ID,
    DELIVERED_TEXT
)

from database import (
    save_mapping,
    get_mapping,
    is_banned
)


def register(client):

    @client.on(events.NewMessage(incoming=True))
    async def relay_message(event):

        if event.sender_id == OWNER_ID:
            return

        if event.raw_text and event.raw_text.startswith("/"):
            return

        if event.message.action:
            return

        if await is_banned(event.sender_id):
            return

        sender = await event.get_sender()

        header = (
            "<b>📨 New Anonymous Message</b>\n\n"
            f"<b>Name:</b> {sender.first_name}\n"
            f"<b>ID:</b> <code>{sender.id}</code>\n\n"
        )

        if event.message.media:

            owner_msg = await client.send_file(
                OWNER_ID,
                event.message.media,
                caption=header + (event.raw_text or ""),
                parse_mode="html"
            )

        else:

            owner_msg = await client.send_message(
                OWNER_ID,
                header + (event.raw_text or ""),
                parse_mode="html"
            )

        await save_mapping(
            owner_msg.id,
            sender.id,
            event.id
        )

        await event.reply(
            DELIVERED_TEXT,
            parse_mode="html"
        )

    @client.on(events.NewMessage(from_users=OWNER_ID))
    async def owner_reply(event):

        if not event.is_reply:
            return

        replied = await event.get_reply_message()

        if not replied:
            return

        data = await get_mapping(replied.id)

        if not data:
            return

        user_id, _ = data

        try:

            if event.message.media:

                await client.send_file(
                    user_id,
                    event.message.media,
                    caption=event.raw_text or ""
                )

            else:

                await client.send_message(
                    user_id,
                    event.raw_text or ""
                )

        except Exception as e:

            await event.reply(
                f"❌ Error:\n<code>{e}</code>",
                parse_mode="html"
            )

