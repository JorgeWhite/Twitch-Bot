"""
    COPYRIGHT INFORMATION

    SOME CODE IN THIS FIEL SIS LICENSED UNDER THE APACHE LICENSE, VERSION 2.0.
    http://aws.amazon.com/apache2.0/
"""
from requests import get
from irc.bot import SingleServerIRCBot

from lib import db, cmds, react, automod

NAME = "YoryiguaitBot"
OWNER = "yoryiguaitbot"
SECOND_OWNER = "jorgewhite"
THIRD_OWNER = "zeratai"
fourth_owner = 'metsteel'

class Bot(SingleServerIRCBot):
    def __init__(self):
        self.HOST = "irc.chat.twitch.tv"
        self.PORT = 6667
        self.USERNAME = NAME.lower()
        self.CLIENT_ID = "7lnwxxbwh8hth4erbvdm1fjj2anf3p"
        self.TOKEN = "1hp340sw8sdwbo7z4ub4r81mustsq5"
        self.CHANNEL = f"#{THIRD_OWNER}"

        url = f"https://api.twitch.tv/kraken/users?login={self.USERNAME}"
        headers = {
            "Client-ID" : self.CLIENT_ID,
            "Accept" : "application/vnd.twitchtv.v5+json"
        }
        resp = get(url, headers = headers).json()
        self.channel_id = resp["users"][0]["_id"]
        
        super().__init__([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")], self.USERNAME, self.USERNAME)

    def on_welcome(self, cxn, event):
        for req in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")

        cxn.join(self.CHANNEL)
        db.build()
        self.send_message("!speak Wenas noches, ijosdesuberga.")

    @db.with_commit
    def on_pubmsg(self, cxn, event):
        tags = {
            kvpair["key"] : kvpair["value"] for kvpair in event.tags
        }
        user = {
            "name" : tags["display-name"],
            "id" : tags["user-id"]
        }
        message = event.arguments[0]

        if user["name"] != NAME and automod.clear(bot, user, message):
            react.process(bot, user, message)
            cmds.process(bot, user, message)

    def send_message(self, message):
        self.connection.privmsg(self.CHANNEL, message)


if __name__ == "__main__":
    bot = Bot()
    bot.start()
