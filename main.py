import logging
import os
import time
import git
import sys

import config
from lib.bot import Bot

# ----------------  Получение обновлений

if config.ENABLE_AUTO_UPDATES:
    g = git.cmd.Git(os.getcwd())
    try:
        if g.pull() != 'Already up to date.':
            print('Программа обновлена. Пожалуйста перезапустите скрипт')
            print('Не забудьте выполнить команду pip install -r requirements.txt перед запуском')
            exit()
    except git.GitCommandError:

        new_path = os.path.dirname(os.getcwd())
        new_dir = new_path + '/amino-bot_NEW'
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)

        git.Git(new_dir).clone("https://github.com/ManKwang/amino-bot.git")

        print('Репозиторий был клонирован в новую папку: ' + new_dir)
        print('Используйте эту папку для работы с ботом')

        os.startfile(new_dir + '/amino-bot')

        exit()

# ---------------- !Получение обновлений

# Initialize the bot
bot = Bot()

if __name__ == '__main__':
    DIR_LOGS = os.getcwd() + '/logs'

    if not os.path.exists(DIR_LOGS):
        os.mkdir(DIR_LOGS)

    DIR_LEN = len([name for name in os.listdir(DIR_LOGS) if os.path.isfile(os.path.join(DIR_LOGS, name))])

    logging.basicConfig(
        handlers=[logging.FileHandler(f"logs/log_{str(DIR_LEN + 1)}.txt", 'w', 'utf-8')],
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        datefmt='%d.%m.%Y %I:%M:%S')

    print('STARTED')
    logging.info('STARTED')
    try:
        bot.run()
        while True:
            time.sleep(470)
            sys.exit()
            #time.sleep(470)
            #bot.run()
    except KeyboardInterrupt:
        print("Бот завершил свою работу")
        logging.info('STOPPED')
        exit()
