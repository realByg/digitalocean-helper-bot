import json
import logging
import traceback
from os import environ
from typing import Union
import urllib.parse as urlparse
from urllib.parse import parse_qs

import telebot
from telebot.types import CallbackQuery, Message

from _bot import bot
# noinspection PyUnresolvedReferences
from modules import *

bot_admins = json.loads(environ.get('bot_admins'))

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

command_dict = {
    '/start': 'start',

    '/aa': 'add_account',
    '/ma': 'manage_accounts',
    '/bta': 'batch_test_accounts',

    '/cd': 'create_droplet',
    '/md': 'manage_droplets',
}


@bot.message_handler(content_types=['text'])
def text_handler(m: Message):
    try:
        logger.info(m)

        if m.from_user.id not in bot_admins:
            return

        if m.text in command_dict.keys():
            globals()[command_dict[m.text]](m)

    except Exception as e:
        traceback.print_exc()
        handle_exception(m, e)


@bot.callback_query_handler(func=lambda call: True)
def callback_query_handler(call: CallbackQuery):
    try:
        logger.info(call)

        if call.from_user.id not in bot_admins:
            return

        callback_data = urlparse.urlparse(call.data)
        func_name = callback_data.path
        data = parse_qs(callback_data.query)
        if func_name in globals():
            args = [call]
            if len(data.keys()) > 0:
                args.append(data)

            globals()[func_name](*args)

    except Exception as e:
        traceback.print_exc()
        handle_exception(call, e)


def handle_exception(d: Union[Message, CallbackQuery], e):
    bot.send_message(
        text=f'出错啦\n'
             f'<code>{e}</code>',
        chat_id=d.from_user.id,
        parse_mode='HTML'
    )
