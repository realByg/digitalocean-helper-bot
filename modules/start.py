from os import environ

from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from _bot import bot

bot_name = environ.get('bot_name', 'Digital Ocean 小助手')


def start(d: Message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton(
            text='添加账号',
            callback_data='add_account'
        ),
        InlineKeyboardButton(
            text='管理账号',
            callback_data='manage_accounts'
        ),
        InlineKeyboardButton(
            text='创建实例',
            callback_data='create_droplet'
        ),
        InlineKeyboardButton(
            text='管理实例',
            callback_data='manage_droplets'
        ),
    )
    t = f'欢迎使用 <b>{bot_name}</b>\n\n' \
        '你可以管理 DigitalOcean 账号，创建实例等\n\n' \
        '快捷命令：\n' \
        '/aa 添加账号  /ma 管理账号  /bta 批量测试账号\n' \
        '/cd 创建实例  /md 管理实例'

    bot.send_message(
        text=t,
        chat_id=d.from_user.id,
        parse_mode='HTML',
        reply_markup=markup
    )
