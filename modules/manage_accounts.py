from typing import Union

from telebot.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from _bot import bot
from utils.db import AccountsDB


def manage_accounts(d: Union[Message, CallbackQuery]):
    t = '<b>管理账号</b>\n\n'
    markup = InlineKeyboardMarkup()

    accounts = AccountsDB().all()

    if len(accounts) == 0:
        t += '没有账号'
        markup.row(
            InlineKeyboardButton(
                text='添加账号',
                callback_data='add_account'
            )
        )

        bot.send_message(
            text=t,
            chat_id=d.from_user.id,
            reply_markup=markup,
            parse_mode='HTML'
        )
        return

    markup.row(
        InlineKeyboardButton(
            text='批量测试',
            callback_data='batch_test_accounts'
        )
    )

    for account in accounts:
        markup.row(
            InlineKeyboardButton(
                text=account.get('email', 'error'),
                callback_data=f'account_detail?doc_id={account.doc_id}'
            )
        )

    bot.send_message(
        text=t,
        chat_id=d.from_user.id,
        reply_markup=markup,
        parse_mode='HTML'
    )
