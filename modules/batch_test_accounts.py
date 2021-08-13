import json
from typing import Union

from telebot.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

import digitalocean
from digitalocean import DataReadError

from _bot import bot
from utils.db import AccountsDB


def batch_test_accounts(d: Union[Message, CallbackQuery]):
    t = '<b>批量测试账号</b>\n\n'
    markup = InlineKeyboardMarkup()

    msg = bot.send_message(
        text=f'{t}'
             f'测试中...',
        chat_id=d.from_user.id,
        parse_mode='HTML',
    )

    accounts = AccountsDB().all()
    checked_accounts = []
    failed_accounts = []

    for account in accounts:
        try:
            account_balance = digitalocean.Balance().get_object(api_token=account['token'])
            account_balance.email = account['email']

            checked_accounts.append(account_balance)

        except DataReadError:
            failed_accounts.append(account['email'])

    t += f'<b>共 {len(accounts)} 个账号</b>\n\n'

    if checked_accounts:
        t += f'测试成功 {len(checked_accounts)} 个：\n'
        for account_balance in checked_accounts:
            t += f'<code>{account_balance.email}</code> | <code>{account_balance.account_balance}</code>\n'
        t += '\n'

    if failed_accounts:
        t += f'测试失败 {len(failed_accounts)} 个：\n'
        for email in failed_accounts:
            t += f'<code>{email}</code>\n'
        markup.add(
            InlineKeyboardButton(
                text='删除失败账号',
                callback_data=json.dumps({
                    't': 'batch_test_delete_accounts'
                })
            )
        )

    bot.edit_message_text(
        text=t,
        chat_id=d.from_user.id,
        message_id=msg.message_id,
        parse_mode='HTML',
        reply_markup=markup
    )
