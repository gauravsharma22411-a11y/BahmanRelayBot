import aiosqlite

DB_PATH = "data/bot.db"


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    joined INTEGER DEFAULT 0,
    banned INTEGER DEFAULT 0,
    first_start INTEGER DEFAULT 1,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS relay(
            owner_msg_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            user_msg_id INTEGER
        )
        """)

        await db.commit()


async def add_user(user):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            INSERT OR IGNORE INTO users
            (user_id, username, first_name)
            VALUES (?, ?, ?)
            """,
            (
                user.id,
                user.username,
                user.first_name
            )
        )
        await db.commit()


async def is_banned(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT banned FROM users WHERE user_id=?",
            (user_id,)
        ) as cur:

            row = await cur.fetchone()

            return bool(row and row[0])


async def ban(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE users SET banned=1 WHERE user_id=?",
            (user_id,)
        )
        await db.commit()


async def unban(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE users SET banned=0 WHERE user_id=?",
            (user_id,)
        )
        await db.commit()


async def save_mapping(owner_msg_id, user_id, user_msg_id):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            INSERT OR REPLACE INTO relay
            (owner_msg_id, user_id, user_msg_id)
            VALUES (?, ?, ?)
            """,
            (
                owner_msg_id,
                user_id,
                user_msg_id
            )
        )
        await db.commit()


async def get_mapping(owner_msg_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            """
            SELECT user_id, user_msg_id
            FROM relay
            WHERE owner_msg_id=?
            """,
            (owner_msg_id,)
        ) as cur:

            return await cur.fetchone()


async def total_users():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT COUNT(*) FROM users"
        ) as cur:

            row = await cur.fetchone()
            return row[0]

async def is_first_start(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT first_start FROM users WHERE user_id=?",
            (user_id,)
        ) as cur:
            row = await cur.fetchone()
            if not row:
                return True
            return bool(row[0])


async def disable_first_start(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE users SET first_start=0 WHERE user_id=?",
            (user_id,)
        )
        await db.commit()
