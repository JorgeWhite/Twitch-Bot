from time import time

from . import misc

PREFIX = "!"

class Cmd(object):
    def __init__(self, callables, func, cooldown):
        self.callables = callables
        self.func = func
        self.cooldown = cooldown
        self.next_use = time()

cmds = [
    Cmd(["hola", "hey"], misc.hello, cooldown=0),
    Cmd(["zeratai", "rafa", "zerato", "rafakin", "enrique", "fafa"], misc.zeratai, cooldown=0),
    Cmd(["channel", "canal"], misc.channel, cooldown=1),
    Cmd(["robvi", "robviplss", "albur"], misc.robvi, cooldown=0),
    Cmd(["robvispeak", "speakrobvi", "alburspeak"], misc.robviSpeak, cooldown=0),
    Cmd(["agregaalbur", "agregarobvi"], misc.agregaRobvi, cooldown=0),
    Cmd(["agregafrase", "addphrase"], misc.addPhrase, cooldown=1),
    Cmd(["frase", "phrase", "freis"], misc.readPhrase, cooldown=1),
    Cmd(["frasespeak", "freisspeak", "speakfrase", "speakfreis"], misc.readPhraseSpeak, cooldown=0),
    Cmd(["chupapi", "chupapimuñaño"], misc.chupapi, cooldown=0),
    Cmd(["songs", "sr", "speak", "game", "title"], misc.nightbot, cooldown=0),
    Cmd(["javo", "javolinkk"], misc.javo, cooldown=1),
    Cmd(["minuta"], misc.minuta, cooldown=0),
    Cmd(["wenas", "buenas"], misc.buenas, cooldown=1),
    Cmd(["gaga", "lthegaga"], misc.gaga, cooldown=0),
    Cmd(["petarda", "morrita", "culito", "potranca"], misc.petarda, cooldown=0),
    Cmd(["agregapetarda", "addpetarda", "agregamorrita", "addmorrita", "agregaculito", "addculito", "agregapotranca"], misc.addPetarda, cooldown=0),
    Cmd(["cripto", "bitcoin", "btc", "criptomoneda"], misc.criptocurrencies, cooldown=0),
    Cmd(["horoscopo"], misc.horoscopo, cooldown=0),
    Cmd(["bufer", "elbufer"], misc.bufer, cooldown=0)
    
]

def process(bot, user, message):
    if message.startswith(PREFIX):
        cmd = message.split(" ")[0][len(PREFIX):]
        cmd = cmd.lower()
        args = message.split(" ")[1:]
        perform(bot, user, cmd, *args)

def perform(bot, user, call, *args):
    if call in ("help", "commands", "cmds"):
        misc.help(bot, PREFIX, cmds)
    else:
        for cmd in cmds:
            if call in cmd.callables:
                if time() > cmd.next_use:
                    cmd.func(bot, user, *args)
                    cmd.next_use = time() + cmd.cooldown
                else:
                    bot.send_message(f"Awanta {user['name']}, hay cooldown")
                return
        bot.send_message(f"{user['name']}, no existe ese comando compa")