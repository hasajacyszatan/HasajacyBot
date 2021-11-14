from os import getenv, getcwd
from telegram import Update
from telegram.ext import CallbackContext
from telegrask.ext import Moderation
from . import bot
from .config import FEDERATION
from .functions import do_action
from .config import HAREGLY
from .config import BLACKLIST
import random
import json
from requests import get
@bot.command("mute", help="zmutuj użytkownika")
def mute(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    do_action(mod, mod.mute)


@bot.command("unmute", help="odmutuj użytkownika")
def mute(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    do_action(mod, mod.unmute)


@bot.command(["ban", "gban", "fban"], help="zbanuj użytkownika w federacji")
def ban(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    do_action(mod, mod.ban, in_federation=mod.chat_id in FEDERATION)

@bot.command(["warn"], help="ucisz niewygodnego użytkownika")
def warn(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    if mod.is_user_admin(update.message.from_user.id):
        mod = Moderation(update, context)
        user_id = update.message["reply_to_message"].from_user.id
        user = update.message["reply_to_message"].from_user.username
        msg = update.message["text"][6:]
        if msg == "clear" or msg == "clean":
            BLACKLIST[user_id] = 0
            update.message.reply_text(f"Użytkownik {user} ma {BLACKLIST[user_id]}/5 ostrzeżeń")
            with open(f"{getcwd()}/data/blacklist.json", "w") as new_blacklist:
                json.dump(BLACKLIST,new_blacklist)
        else:
            if not msg.isdigit() or int(msg) < 1:
                msg = 0
            if user_id in BLACKLIST:
                BLACKLIST[user_id] += int(msg)
            else:
                BLACKLIST[user_id] = int(msg)
            print(BLACKLIST)
            with open(f"{getcwd()}/data/blacklist.json", "w") as new_blacklist:
                json.dump(BLACKLIST,new_blacklist)
            update.message.reply_text(f"Użytkownik {user} otrzymał {BLACKLIST[user_id]}/5 ostrzeżeń")
            if BLACKLIST[user_id] > 5:
                mod = Moderation(update, context)
                do_action(mod, mod.ban, in_federation=mod.chat_id in FEDERATION)
    else:
        update.message.reply_text("nie masz odpowiednich uprawnień")
@bot.command("unban", help="odbanuj użytkownika w federacji")
def unban(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    do_action(mod, mod.unban, in_federation=mod.chat_id in FEDERATION)

@bot.command("haregly", help="pokazuje losową wiadomość hareglyego")
def haregly(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    try:
        reply_id = update.message["reply_to_message"].message_id
    except:
        reply_id = None
    context.bot.delete_message(chat_id, update.message.message_id)
    context.bot.send_message(chat_id, HAREGLY[random.randrange(0, len(HAREGLY))], reply_to_message_id=reply_id)

@bot.command("haregly_add", help="dodaje wiadomość hareglyego do spywaru")
def haregly(update: Update, context: CallbackContext):
    msg = update.message["reply_to_message"].text
    HAREGLY.append(msg)
    with open(f"{getcwd()}/data/haregly.json", "w") as new_haregly:
            json.dump(HAREGLY,new_haregly)

@bot.command("covid_daily", help="podaje wczorajszą informacje o liczbie chorych na covid")
def covid(update: Update, context: CallbackContext):
    update.message.reply_text(get("https://koronawirus-api.herokuapp.com/api/covid19/daily").json()['today']['newInfections'])
