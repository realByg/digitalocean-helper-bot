from os import environ

import telebot

bot_token = environ.get('bot_token')

bot = telebot.TeleBot(token=bot_token)
