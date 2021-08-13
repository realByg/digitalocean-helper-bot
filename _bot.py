from os import environ

import telebot

bot_token = environ.get('bot_token', '1713484373:AAHGixhUMqwYlioXtR-thdG-ZYi0Tw_WpXk')

bot = telebot.TeleBot(token=bot_token)
