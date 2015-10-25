#!/usr/bin/env python
import telebot
import pylast
import json

config = json.load(open("config.json"))
TOKEN = config["TOKEN"]
lastfm_apikey = config["lastfm_apikey"]
lastfm_apisecret = config["lastfm_apisecret"]
bot = telebot.TeleBot(TOKEN)

def lastfm_parse(message):
    lastfm = pylast.LastFMNetwork(lastfm_apikey, lastfm_apisecret)
    message_arguments = message.text.split(" ")
    lastfm_username = message_arguments[1] if len(message_arguments) == 2 else (message.from_user.username if message.from_user.username != None and message.from_user.username != "" else "citizenwasp")
    current_track = lastfm.get_user(lastfm_username).get_now_playing()

    if (current_track == None or current_track == ""):
        current_track = lastfm_username + " is not scrobbling!"

    return current_track


@bot.message_handler(commands=["lastfm"])
def lastfm_reply(message):
    bot.reply_to(message, lastfm_parse(message))

bot.polling()