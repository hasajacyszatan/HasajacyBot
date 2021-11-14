from telegrask.ext import Moderation, UserURL
from typing import Callable
from .config import FEDERATION


def do_action(mod: Moderation, method: Callable, in_federation: bool = False):
    update, context = mod.update, mod.context
    user = update.message["reply_to_message"].from_user
    user_url = UserURL(user)

    activities = {
        "mute": "zmutowany",
        "unmute": "odmutowany",
        "ban": "zbanowany",
        "unban": "odbanowany",
    }

    msg = f"ℹ Użytkownik {user_url} został {activities[method.__name__]}\."

    try:
        if mod.is_user_admin(update.message.from_user.id):
            update.message.reply_text("❌ Nie masz wystarczających uprawnień.")
        else:
            update.message.reply_text("❌ Nie masz wystarczających uprawnień.")
    except PermissionError:
        update.message.reply_text("❌ Błąd uprawnień.")