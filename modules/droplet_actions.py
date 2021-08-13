from telebot.types import CallbackQuery

import digitalocean

from _bot import bot
from utils.db import AccountsDB


def droplet_actions(call: CallbackQuery, data: dict):
    doc_id = data['doc_id'][0]
    droplet_id = data['droplet_id'][0]
    action = data['a'][0]

    account = AccountsDB().get(doc_id=doc_id)
    droplet = digitalocean.Droplet(
        token=account['token'],
        id=droplet_id
    )

    if action in globals():
        globals()[action](call, droplet)


# def change_ip(call: CallbackQuery, droplet: digitalocean.Droplet):
#     bot.edit_message_text(
#         text=f'{call.message.html_text}\n\n'
#              '<b>实例更换 IP 中...</b>',
#         chat_id=call.from_user.id,
#         message_id=call.message.message_id,
#         parse_mode='HTML'
#     )
#
#     droplet.load()
#
#     bot.edit_message_text(
#         text=f'{call.message.html_text}\n\n'
#              '<b>实例更换 IP 完成，请刷新</b>',
#         chat_id=call.from_user.id,
#         message_id=call.message.message_id,
#         reply_markup=call.message.reply_markup,
#         parse_mode='HTML'
#     )


def delete(call: CallbackQuery, droplet: digitalocean.Droplet):
    bot.edit_message_text(
        text=f'{call.message.html_text}\n\n'
             '<b>实例删除中...</b>',
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        parse_mode='HTML'
    )

    droplet.load()
    droplet.destroy()

    bot.edit_message_text(
        text=f'{call.message.html_text}\n\n'
             f'<b>实例已删除</b>',
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        parse_mode='HTML'
    )


def shutdown(call: CallbackQuery, droplet: digitalocean.Droplet):
    bot.edit_message_text(
        text=f'{call.message.html_text}\n\n'
             '<b>实例关机中，请稍后刷新</b>',
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        reply_markup=call.message.reply_markup,
        parse_mode='HTML'
    )

    droplet.load()
    droplet.shutdown()


def reboot(call: CallbackQuery, droplet: digitalocean.Droplet):
    bot.edit_message_text(
        text=f'{call.message.html_text}\n\n'
             '<b>实例重启中，请稍后刷新</b>',
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        reply_markup=call.message.reply_markup,
        parse_mode='HTML'
    )

    droplet.load()
    droplet.reboot()


def power_on(call: CallbackQuery, droplet: digitalocean.Droplet):
    bot.edit_message_text(
        text=f'{call.message.html_text}\n\n'
             '<b>实例开机中，请稍后刷新</b>',
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        reply_markup=call.message.reply_markup,
        parse_mode='HTML'
    )

    droplet.load()
    droplet.reboot()
