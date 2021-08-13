from telebot.types import CallbackQuery

from _bot import bot
from utils.db import AccountsDB


def delete_account(call: CallbackQuery, data: dict):
    doc_id = data['doc_id'][0]

    AccountsDB().remove(doc_id=doc_id)

    bot.edit_message_text(
        text=f'{call.message.html_text}\n\n'
             f'<b>账号已删除</b>',
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        parse_mode='HTML'
    )
