from telethon.tl.types import User
from config import OWNER_ID


def mention(user: User):
    """Return HTML mention for a user."""
    name = user.first_name or "User"
    return f'<a href="tg://user?id={user.id}">{name}</a>'


def is_owner(user_id: int):
    """Check if sender is bot owner."""
    return user_id == OWNER_ID


def build_user_info(user: User):
    """Format user information for owner."""

    username = (
        f"@{user.username}"
        if user.username
        else "No Username"
    )

    return (
        f"<b>👤 New Message</b>\n\n"
        f"<b>Name:</b> {user.first_name}\n"
        f"<b>Username:</b> {username}\n"
        f"<b>ID:</b> <code>{user.id}</code>"
    )
