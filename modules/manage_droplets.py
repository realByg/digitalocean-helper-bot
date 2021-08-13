from typing import Union

from telebot.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from _bot import bot
from utils.db import AccountsDB


def manage_droplets(d: Union[Message, CallbackQuery]):
    t = '<b>管理实例</b>\n\n'
    markup = InlineKeyboardMarkup()

    accounts = AccountsDB().all()

    if len(accounts) == 0:
        markup.row(
            InlineKeyboardButton(
                text='添加账号',
                callback_data='add_account'
            )
        )

        bot.send_message(
            text=f'{t}'
                 f'你还没有添加账号',
            chat_id=d.from_user.id,
            reply_markup=markup,
            parse_mode='HTML'
        )
        return

    for account in accounts:
        markup.add(
            InlineKeyboardButton(
                text=account['email'],
                callback_data=f'list_droplets?doc_id={account.doc_id}'
            )
        )

    bot.send_message(
        text=f'{t}'
             f'请选择账号',
        chat_id=d.from_user.id,
        parse_mode='HTML',
        reply_markup=markup
    )
