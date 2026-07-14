from telethon import events

from config import OWNER_ID
from database import get_mapping


def register(client):

    @client.on(events.NewMessage(from_users=OWNER_ID))
    async def owner_reply(event):

        if not event.is_reply:
            return

        reply = await event.get_reply_message()

        if not reply:
            return

        data = await get_mapping(reply.id)

        if not data:
            return

        user_id, _ = data

        try:

            if event.raw_text:

                await client.send_message(
                    user_id,
                    event.raw_text
                )

            elif event.media:

                await client.send_file(
                    user_id,
                    event.media,
                    caption=event.raw_text or ""
                )

        except Exception as e:

            await event.reply(
                f"❌ Failed to send reply.\n\n{e}"
            )
