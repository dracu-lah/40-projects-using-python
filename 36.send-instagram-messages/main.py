# pip install instabot

from instabot import Bot
bot = Bot()

bot.login(username="Sender username", password="Sender password")
bot.send_message("message", ["Reciever username"])
