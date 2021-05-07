from collections import defaultdict
from . import db

CURSES = ()
warning_timers = (1, 5, 60)

def clear(bot, user, message):

    if any([curse in message for curse in CURSES]):
        warn(bot, user, reason="grosero")
        return False
    return True

def warn(bot, user, *, reason=None):
    warnings = db.field("SELECT Warnings FROM users WHERE UserID = ?", user["id"])

    if warnings < len(warning_timers):
        mins = warning_timers[warnings]
        bot.send_message(f"/timeout {user['name']} {mins}m")
        bot.send_message(f"c va muteado {user['name']} por {reason}, regresas en {mins} minutos.")

        db.execute("UPDATE users SET Warnings = Warnings + 1 WHERE UserID = ?", user["id"])
    else:
        bot.send_message(f"c va baneado {user['name']}")
