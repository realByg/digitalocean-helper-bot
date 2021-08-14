def parse_config():
    import json
    from os import environ

    config = json.load(open('config.json', 'r', encoding='utf-8'))
    environ['bot_name'] = config['BOT']['NAME']
    environ['bot_token'] = config['BOT']['TOKEN']
    environ['bot_admins'] = json.dumps(config['BOT']['ADMINS'])


def start_bot():
    from bot import bot

    bot.polling(none_stop=True)


if __name__ == '__main__':
    parse_config()
    start_bot()
