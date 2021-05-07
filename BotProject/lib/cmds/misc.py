import time
import random_number as rn
import requests



def help(bot, prefix, cmds):
    bot.send_message("Registered commands: "
                     + ", ".join([f"{prefix}{cmd.callables[0]}" for cmd in sorted(cmds, key=lambda cmd: cmd.callables[0 ])]))

def hello(bot, user, *args):
    bot.send_message(f"K onda {user['name']}!")

def zeratai(bot, user, *args):
    responses = ["Denle follow al @zeratai ijosdelaberga", "Sigan al rafakin", "Sigan a enrique",
                 "Denle follow a Fafa", "Denle follow a kikin rafakin"]
    random = rn.random_number(0, len(responses) - 1)
    responseIndex = rn.random_number.get_random_number(random)
    bot.send_message(responses[responseIndex] + f" https://www.twitch.tv/zeratai")

def channel(bot, user, *args):
    channel = args[0][1:]
    url = f"https://www.twitch.tv/{channel}"
    responses = [f"Sigan a este ijodelaberga hermoso " + url,
                 f"Den follow a " + url + " hermoso",
                 f"Ijosdelaberga, denle follow a " + url,
                 ]
    random = rn.random_number(0, len(responses) - 1)
    responseIndex = rn.random_number.get_random_number(random)

    bot.send_message(responses[responseIndex])

def chupapi(bot, user, *args):
    bot.send_message(f"Chupapi muñaño")

def robvi(bot, user, *args):
    if len(args) == 0:
        f = open("frases_robvi.txt", "r")
        f0 = f.readlines()
        lines = 0
        for x in f0:
            lines += 1
        f.close()

        random = rn.random_number(2, lines)
        phraseNumber = rn.random_number.get_random_number(random)
        file = open("frases_robvi.txt", "r")
        f1 = file.readlines()
        line = 1
        for x in f1:
            if line == phraseNumber:
                x_ascii = ascii(x)
                x_ascii = x_ascii[1:-3]
                bot.send_message(x_ascii)
                return
            line += 1
    else:
        f = open("frases_robvi.txt", "r")
        f0 = f.readlines()
        line = 0
        for x in f0:
            line += 1
            if str(line) == (args[0]):
                x_ascii = ascii(x)
                x_ascii = x_ascii[1:-3]
                bot.send_message(x_ascii)
                f.close()
                return

def robviSpeak(bot, user, *args):
    if len(args) == 0:
        f = open("frases_robvi.txt", "r")
        f0 = f.readlines()
        lines = 0
        for x in f0:
            lines += 1
        f.close()

        random = rn.random_number(2, lines)
        phraseNumber = rn.random_number.get_random_number(random)
        file = open("frases_robvi.txt", "r")
        f1 = file.readlines()
        line = 1
        for x in f1:
            if line == phraseNumber:
                x_ascii = ascii(x)
                x_ascii = x_ascii[1:-3]
                bot.send_message("!speak " + x_ascii)
                return
            line += 1
    else:
        f = open("frases_robvi.txt", "r")
        f0 = f.readlines()
        line = 0
        for x in f0:
            line += 1
            if line == int(args[0]):
                x_ascii = ascii(x)
                x_ascii = x_ascii[1:-3]
                bot.send_message("!speak " + x_ascii)
                f.close()
                return

def javo(bot, user, *args):
    responses = ["javinski", "javeivi", "c viene", "asuberga te voa quedar mal", "perrufianes", "todo pendo"]
    random = rn.random_number(0, len(responses) - 1)
    responseIndex = rn.random_number.get_random_number(random)
    bot.send_message(responses[responseIndex])

def readPhrase(bot, user, *args):
    if len(args) == 0:
        f = open("frases.txt", "r")
        f0 = f.readlines()
        lines = 0
        for x in f0:
            lines += 1
        f.close()

        random = rn.random_number(1, lines)
        phraseNumber = rn.random_number.get_random_number(random)
        file = open("frases.txt", "r")
        f1 = file.readlines()
        line = 1
        for x in f1:
            if line == phraseNumber:
                x_ascii = ascii(x)
                x_ascii = x_ascii[1:-3]
                bot.send_message(x_ascii)
                return
            line += 1
    else:
        f = open("frases.txt", "r")
        f0 = f.readlines()
        line = 0
        for x in f0:
            line += 1
            if str(line) == (args[0]):
                x_ascii = ascii(x)
                x_ascii = x_ascii[1:-3]
                bot.send_message(x_ascii)
                f.close()
                return

def readPhraseSpeak(bot, user, *args):
    if len(args) == 0:
        f = open("frases.txt", "r")
        f0 = f.readlines()
        lines = 0
        for x in f0:
            lines += 1
        f.close()

        random = rn.random_number(1, lines)
        phraseNumber = rn.random_number.get_random_number(random)
        file = open("frases.txt", "r")
        f1 = file.readlines()
        line = 1
        for x in f1:
            if line == phraseNumber:
                x_ascii = ascii(x)
                x_ascii = x_ascii[1:-3]
                bot.send_message("!speak " + x_ascii)
                return
            line += 1
    else:
        f = open("frases.txt", "r")
        f0 = f.readlines()
        line = 0
        for x in f0:
            line += 1
            if str(line) == (args[0]):
                x_ascii = ascii(x)
                x_ascii = x_ascii[1:-3]
                bot.send_message("!speak " + x_ascii)
                f.close()
                return

def addPhrase(bot, user, *args):
    ## Write the phrase
    phrase = ""
    for i in range(len(args)):
        phrase += args[i]
        phrase += " "
    f = open("frases.txt", "a+")
    f.write(phrase + "\r\n")
    f.close()

    ## Count the number of lines
    f = open("frases.txt", "r")
    f0 = f.readlines()
    lines = 0
    for x in f0:
        lines += 1
    f.close()

    responses = ["Listo compa", "Frase agregada compa", "Wena frase", "Hermosa frase", "Frase meh", "Frase tranqui"]
    random = rn.random_number(1, len(responses) - 1)
    responseNumber = rn.random_number.get_random_number(random)
    bot.send_message(responses[responseNumber] + ", frase #" + str(lines))

def agregaRobvi(bot, user, *args):
    ## Write the phrase
    phrase = ""
    for i in range(len(args)):
        phrase += args[i]
        phrase += " "
    f = open("frases_robvi.txt", "a+")
    f.write(phrase + "\r\n")
    f.close()

    ## Count the number of lines
    f = open("frases_robvi.txt", "r")
    f0 = f.readlines()
    lines = 0
    for x in f0:
        lines += 1
    f.close()

    responses = ["Listo compa", "Albur agregado compa", "Que avanzado", "Hermoso albur", "Albur meh", "Albur tranqui"]
    random = rn.random_number(1, len(responses) - 1)
    responseNumber = rn.random_number.get_random_number(random)
    bot.send_message(responses[responseNumber] + ", albur #" + str(lines))


def nightbot(bot, user, *args):
    return

def horoscopo(bot, user, *args):
    if len(args) == 0:
        bot.send_message(f"Dime tu signo ijodelaberga {user['name']}")
        return
    sunsign = args[0].lower()

    validSunsings = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius",
                     "capricorn", "aquarius", "pisces"]
    if sunsign not in validSunsings:
        bot.send_message(f'Los signos son Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, ' +
                     'Capricorn, Aquarius, Pisces')
        return
    params = (
        ('sign', sunsign),
        ('day', 'today'),
    )
    response = requests.post('https://aztro.sameerkumar.website/', params=params)
    horoscope = response.json()
    bot.send_message(sunsign + " " +  horoscope['description'])


def minuta(bot, user, *args):
    bot.send_message(f"!speak minuta del 15 de abril del 2021. Empieza del mame de @zeratai con @DarkYoryitou y @DarkYizusm, "
                     f"Press F para los que estudiaron comunicación, el servicio militar le cambió la vida a @DanAragon, "
                     f"@maverickytdg2 tardando media hora en irse del stream, "
                     f"@angelabadalamenti se entera del beso de @zeratai, "
                     f"@alkxofitas master de red dead online, "
                     f"7 meses de @edgardo_martinez_p uno de los primeros subscriptores")
    time.sleep(2)
    bot.send_message(f"!speak c viene @JavoLINKK le ofrecen melon y medio para su vivienda"
                     f" a eso súmenle 16 pesos de bitcoin que minó, "
                     f"@zeratai y @jorgewhite reconocen sus errores y se perdonan, "
                     f"@zeratai traicionando a @edgardo_martinez_p porque nunca va a jugar the witness, "
                     f"raid a @Sr_pixel_ termina mal, @sr_pixel_ le dice pandoras a @PANODRAMAS")

def buenas(bot, user, *args):
    bot.send_message(f"Buenas noches, ijosdesuberga")

def gaga(bot, user, *args):
    phrases = [f"L de Lady Gaga", "No tengas miedo porque soy de Sinaloa"]
    bot.send_message(randomResponse(phrases))

def randomResponse(phrases):
    random = rn.random_number(0, len(phrases) - 1)
    responseIndex = rn.random_number.get_random_number(random)
    return phrases[responseIndex]

def petarda(bot, user, *args):
    if len(args) == 0:
        f = open("petardas.txt", "r")
        f0 = f.readlines()
        lines = 0
        for x in f0:
            lines += 1
        f.close()

        random = rn.random_number(1, lines)
        phraseNumber = rn.random_number.get_random_number(random)
        file = open("petardas.txt", "r")
        f1 = file.readlines()
        line = 1
        for x in f1:
            if line == phraseNumber:
                x_ascii = ascii(x)
                x_ascii = x_ascii[1:-3]
                bot.send_message(x_ascii)
                return
            line += 1
    else:
        f = open("petardas.txt", "r")
        f0 = f.readlines()
        line = 0
        for x in f0:
            line += 1
            if str(line) == (args[0]):
                x_ascii = ascii(x)
                x_ascii = x_ascii[1:-3]
                bot.send_message(x_ascii)
                f.close()
                return


def addPetarda(bot, user, *args):
    ## Write the phrase
    phrase = ""
    for i in range(len(args)):
        phrase += args[i]
        phrase += " "
    f = open("petardas.txt", "a+")
    f.write(phrase + "\r\n")
    f.close()

    ## Count the number of lines
    f = open("petardas.txt", "r")
    f0 = f.readlines()
    lines = 0
    for x in f0:
        lines += 1
    f.close()

    responses = ["Listo compa", "Waxando culos", "Morrita tranqui", "Petarda meh", "Petarda tranqui",
                 "Potranca tranqui", "Buena potranca", "Gran potranca"]
    random = rn.random_number(1, len(responses) - 1)
    responseNumber = rn.random_number.get_random_number(random)
    bot.send_message(responses[responseNumber] + ", morrita #" + str(lines))

def criptocurrencies(bot, user, *args):
    if len(args) == 0:
        bot.send_message(f"Dime de que moneda ijodelaberga {user['name']}")
        return
    coin = args[0].upper()
    validCoins = {
        'BTC': '90',
        'ADA': '257',
        'EASY': '46189',
        'ONE': '48567',
        'SHIB': '45088',
        'ETH': '80',
        'LTC': '1',
        'BNB': '2710'
    }
    if coin in validCoins:
        url = "https://api.coinlore.net/api/ticker/?id="
        response = requests.get(url + validCoins[coin])
        price = response.json()
        price_parsed = price[0]['price_usd']
        bot.send_message(f"!speak El precio actual de {coin} es de {price_parsed} usd ijosdelaberga")
    else:
        bot.send_message(f"Las monedas disponibles son BTC, ETH, BNB, ADA, EASY, ONE, SHIB y LTC")

def bufer(bot, user, *args):
    responses = [f"!speak Que descanse en paz @elbufer.", f"!speak @ElBufer oficialmente terminó transmisiones "
                                                          f"el 17 de marzo del 2021"]
    bot.send_message(randomResponse(responses))
