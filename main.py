from telethon import TelegramClient

from config import API_ID, API_HASH, BOT_TOKEN
from database import init_db

from handlers import start
from handlers import relay
from handlers import admin
from handlers import callbacks


client = TelegramClient(
    "bahman_bot",
    API_ID,
    API_HASH
).start(bot_token=BOT_TOKEN)


async def startup():
    await init_db()


def register_handlers():
    start.register(client)
    relay.register(client)
    admin.register(client)
    callbacks.register(client)


async def main():
    await startup()
    register_handlers()

    print("===================================")
    print("  BAHMAN RELAY BOT STARTED 🚀")
    print("===================================")

    await client.run_until_disconnected()


with client:
    client.loop.run_until_complete(main())
