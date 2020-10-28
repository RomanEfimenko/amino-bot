import json
import os
import time

from amino.client import Client
from lib.MessageHandler import MessageHandler
from lib.logger import log



class Bot:
    """
    The main class
    """

    def __init__(self):
        """
        Initializing method
        """

        self.client = Client()
        self.bot_start = False

        # Check if config file exists
        if not os.path.exists(os.getcwd() + '/config.json'):
            print("Для начала нужно ввести данные для авторизации")
            self.login = input("Введите ваш логин: ")
            self.password = input("Введите ваш пароль: ")

            with open(os.getcwd() + '/config.json', 'w', encoding='UTF-8') as config_file:
                config_file.write(json.dumps({'login': self.login, 'password': self.password}))
                config_file.close()

            log("Файл конфигурации успешно создан")
        else:
            with open(os.getcwd() + '/config.json') as config_file:
                data = json.loads(config_file.read())
                config_file.close()

            self.login = data['login']
            self.password = data['password']

    def run(self):
        if self.bot_start == False:
            self.log_in()
            self.choose_amino()
            self.choose_chats()
            self.client.callbacks = MessageHandler(self.client, self.selected_chats)
            self.bot_start = True
        else:
            log("Повторное создание клиента")
            self.client = None
            self.client = Client()
            self.log_in()
            self.client.callbacks = MessageHandler(self.client, self.selected_chats)

    def log_in(self):
        """
        Logging in to an account and choosing amino, chats
        """
        log("Пытаюсь войти в Амино...")
        self.client.login(self.login, self.password)
        if self.client.authenticated:
            log("Авторизация прошла успешно")
        else:
            log("Ошибка авторизации! Проверьте правильно ли вы ввели данные")
            log("Удалите файл config.json для повторного ввода")
            exit()

    def choose_amino(self):
        """
        Choosing an amino to work with
        """

        # Get amino list
        amino_list = []
        c = 1
        aminos = {}
        for i in self.client.sub_clients:
            aminos[c] = i
            print(str(c) + ". " + i)

            c += 1

        #self.selected_amino = aminos[int(input("Выберите одно из амино: "))]#1 test 2 lampovie
        self.selected_amino = aminos[int("2")]
        log(f"Вы выбрали {self.selected_amino}")
        print()

    def choose_chats(self):
        """
        Choosing chats of amino to monitor
        """
        self.chats = self.client.sub_clients[self.selected_amino].chat_threads
        c = 0
        for i in self.chats:
            if not i.title:
                print(str(c) + '. приватный чат')
                c += 1
                continue

            print(str(c) + '. ' + i.title)
            c += 1

        #selected_chats = input("Окей, теперь выбери чаты через запятую (например 0,2,3): ").split(',')#0 тестовый чат/18+ люда
        selected_chats = "0,1,2".split(',')
        self.selected_chats = []
        for i in selected_chats:
            self.selected_chats.append(self.chats[int(i)])
            if not self.chats[int(i)].title:
                log("Начинаю мониторить приватный чат")
                continue
            log("Начинаю мониторить чат " + self.chats[int(i)].title)
