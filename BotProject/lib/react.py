from collections import defaultdict
import random_number as rn

from . import db

welcomed = []
messages = defaultdict(int)

def process(bot, user, message):
    update_records(bot, user)
    if user["id"] not in welcomed:
        username = user['name'].lower()
        if username == "angielglez":
            welcomeLala(bot, user)
        welcome(bot, user)
    elif "bais" in message:
        say_goodbye(bot, user)
    check_activity(bot, user)

def update_records(bot, user):
    db.execute("INSERT OR IGNORE INTO users (UserID) VALUES (?)", user["id"])

    db.execute("UPDATE users SET MessagesSent = MessagesSent + 1 WHERE UserID = ?", user["id"])

def welcome(bot, user):
    phrases = [f"Wenas {user['name']}, ijodelaberga",
               f"Saludos cordiales {user['name']}",
               f"Llegó {user['name']}, hermoso",
               f"Bienvenido ijodelaberga {user['name']}",
               f"Buenas las tengas {user['name']}",
               f"Que onda, {user['name']}",
               f"K onda ijodelaberga {user['name']}"
               ]
    random = rn.random_number(0, len(phrases) - 1)
    phraseIndex = rn.random_number.get_random_number(random)
    bot.send_message(phrases[phraseIndex])
    welcomed.append(user["id"])


def welcomeLala(bot, user):
    bot.send_message(f"!speak @Angielglez está en el stream, esto no es un simulacro.")


def say_goodbye(bot, user):
    bot.send_message(f"Adios {user['name']}, ijodelaberga")
    welcomed.remove(user["id"])

def check_activity(bot, user):
    messages[user["id"]] += 1

    if (count := messages[user["id"]]) % 60 == 0:
        bot.send_message(f"Hermoso {user['name']}, 60 mensajes, ijodelaberga")