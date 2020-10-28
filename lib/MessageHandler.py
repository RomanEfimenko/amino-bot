import os

import lib.warning as warning
from amino.socket import Callbacks
from lib.logger import log
from lib.obscene import Obscene
import time
import datetime
import random


class MessageHandler(Callbacks):
    def __init__(self, client, selected_chats):
        """
        Build the callback handler.
        This is meant to be subclassed, where desided methods would be redefined.
        client: Client to be used
        """
        self.client = client
#        self.auto_sms()
        self.private_chat_for_spam = False
        self.methods = {
            1000: self._resolve_chat_message
        }

        self.chat_methods = {
            "0:0": self.on_text_message,
            "0:100": self.on_image_message,
            "0:103": self.on_youtube_message,

            "2:110": self.on_voice_message,

            "3:113": self.on_sticker_message,

            "101:0": self.on_group_member_join,
            "102:0": self.on_group_member_leave,
            "103:0": self.on_chat_invite
        }

        self.selected_chats = selected_chats

        with open(os.getcwd() + '/warning.txt', 'r', encoding='UTF-8') as warning_file:
            self.warning_text = warning_file.read()
            warning_file.close()

        with open(os.getcwd() + '/data/txt/hi18chat.txt', 'r', encoding='UTF-8') as hi18chat_file:
            self.hi18chat_text = hi18chat_file.read()
            hi18chat_file.close()

        with open(os.getcwd() + '/data/txt/hi18chat2.txt', 'r', encoding='UTF-8') as hi18chat2_file:
            self.hi18chat2_text = hi18chat2_file.read()
            hi18chat2_file.close()

        with open(os.getcwd() + '/data/txt/hi18chat3.txt', 'r', encoding='UTF-8') as hi18chat3_file:
            self.hi18chat3_text = hi18chat3_file.read()
            hi18chat3_file.close()

    def on_text_message(self, data):
        data = data['o']['chatMessage']
        user_id = data['author']['uid']
        user_reputation = data['author']['reputation']
        user_nickname = data['author']['nickname']
        user_level = data['author']['level']
        thread_id = data['threadId']
        message_text = data['content']
        #Если смс от бота, он не реагирует.
        if user_id == self.client.uid:
            return False
        if user_nickname == "Линчеватель":
            user_nickname = "Лянча"
        if user_nickname == "denvin":
            user_nickname = "Скунс"
        ob = Obscene()



        for i in self.selected_chats:
            #log(message_text)
            #атюки
            #if  self.private_chat_for_spam == False and i.uid == thread_id:
                #self.private_chat_for_spam == True
                #self.auto_sms(i)
            if i.uid == thread_id and (message_text.lower()).find('цаца шлюха') != -1:
                log(str(datetime.datetime.now())+" Функция - цаца шлюха")
                i.send_text_message(user_nickname+", мамку твою раком трахала)")
                return True
            if i.uid == thread_id and (message_text.lower()).find('цаца стерва') != -1:
                log(str(datetime.datetime.now())+" Функция - цаца стерва")
                i.send_text_message(user_nickname+", в сраку твого батю перла,)")
                return True
            if i.uid == thread_id and (message_text.lower()).find('цаца салам') != -1:
                log(str(datetime.datetime.now())+" Функция - цаца салам")
                i.send_text_message(user_nickname+", аллейкум салам")
                return True
            if i.uid == thread_id and (message_text.lower()).find('цаца привет') != -1 or (message_text.lower()).find('цаца ку') != -1 or (message_text.lower()).find('цаца здравствуй') != -1:
                log(str(datetime.datetime.now())+" Функция - цаца привет")
                i.send_text_message(user_nickname+", салам")
                return True
            if i.uid == thread_id and not ob.is_clear(message_text):
                user_warnings = warning.warning(user_id)
                log(f"Пользователь {user_nickname} ({user_warnings}) нарушает правила сообщества в чате {i.title}.")
                i.send_text_message(self.warning_text.replace('{name}', user_nickname).replace('{warnings}', str(user_warnings)))
                return True
            if i.uid == thread_id and ((message_text.lower()).find('линч это копенгаген') != -1 or (message_text.lower()).find('линч це копенгаген') != -1 or (message_text.lower()).find('линчеватель це копенгаген') != -1 or (message_text.lower()).find('линчеватель это копенгаген') != -1):
                log(str(datetime.datetime.now())+" Функция - линч это")
                i.send_text_message(user_nickname+", максимум Дублин")
                return True
            if i.uid == thread_id and ((message_text.lower()).find('линч это дублин') != -1 or (message_text.lower()).find('линч це дублин') != -1 or (message_text.lower()).find('линчеватель це дублин') != -1 or (message_text.lower()).find('линчеватель это дублин') != -1):
                log(str(datetime.datetime.now())+" Функция - линч это")
                i.send_text_message(user_nickname+", максимум Харьков")
                return True
            if i.uid == thread_id and ((message_text.lower()).find('линч это харьков') != -1 or (message_text.lower()).find('линч це харьков') != -1 or (message_text.lower()).find('линчеватель це харьков') != -1 or (message_text.lower()).find('линчеватель это харьков') != -1):
                log(str(datetime.datetime.now())+" Функция - линч это")
                i.send_text_message(user_nickname+", да, одноветочный.")
                return True
            if i.uid == thread_id and (message_text.lower()).find('люда з села') != -1 or (message_text.lower()).find('люда з сила') != -1:
                log(str(datetime.datetime.now())+" Функция - люда з села")
                i.send_text_message(user_nickname+", ага, із забитого нахуй.")
                return True
            if i.uid == thread_id and (message_text.lower()).find('стелла собака') != -1:
                log(str(datetime.datetime.now())+" Функция - стелла собака")
                i.send_text_message(user_nickname+", вроді гавкає.")
                return True
            if i.uid == thread_id and (message_text.lower()).find('кусь токсик') != -1:
                log(str(datetime.datetime.now())+" Функция - кусь токсик")
                i.send_text_message(user_nickname+", кто такой єтот ваш кусь?")
                return True
            if i.uid == thread_id and (message_text.lower()).find('го гс') != -1:
                log(str(datetime.datetime.now())+" Функция - го гс")
                i.send_text_message(user_nickname+", опять по бл**ям? Ви ж старі як дінозаври..")
                return True
            if i.uid == thread_id and (message_text.lower()).find('кпоп норм') != -1:
                log(str(datetime.datetime.now())+" Функция - кпоп норм")
                i.send_text_message(user_nickname+", а твоє єбало нє норм")
                return True
            if i.uid == thread_id and (message_text.lower()).find('цаца крутая') != -1 or (message_text.lower()).find('цаца классная') != -1 or (message_text.lower()).find('цаца хорошая') != -1:
                log(str(datetime.datetime.now())+" Функция - цаца крутая")
                i.send_text_message(user_nickname+", спасибо, а ты секс :3")
                return True
            if i.uid == thread_id and (message_text.lower()).find('цаца бот') != -1 or (message_text.lower()).find('цаца робот') != -1 or (message_text.lower()).find('цаца компютер') != -1:
                log(str(datetime.datetime.now())+" Функция - цаца бот")
                i.send_text_message(user_nickname+", я думала ти мені друг((")
                return True
            if i.uid == thread_id and ((message_text.lower()).find('рома бандера') != -1 or (message_text.lower()).find('рома укроп') != -1 or (message_text.lower()).find('рома хохол') != -1):
                log(str(datetime.datetime.now())+" Функция - рома бандера")
                i.send_text_message(user_nickname+", Рома бог, а ти сосеш.")
                return True
            if i.uid == thread_id and (message_text.lower()).find('давно тебя не было в уличных гонках') != -1:
                log(str(datetime.datetime.now())+" Функция - уличные гонки")
                i.send_text_message(user_nickname+", так пизданула наче Іван Солярка.")
                return True
            if i.uid == thread_id and (message_text.lower()).find('хохлушка') != -1:
                log(str(datetime.datetime.now())+" Функция - хохлушка")
                i.send_text_message(user_nickname+", не хохлушка а багіня.")
                return True
            if i.uid == thread_id and (message_text.lower()).find('вы все зёпы') != -1:
                log(str(datetime.datetime.now())+" Функция - Вы все зёпы")
                i.send_text_message(user_nickname+", посмокчи мою чорну єлду.")
                return True
            if i.uid == thread_id and (message_text.lower()).find('рома алкаш') != -1:
                log(str(datetime.datetime.now())+" Функция - рома алкаш")
                i.send_text_message(user_nickname+", Рома професійний соміль'є.")
                return True
            if i.uid == thread_id and (message_text.lower()).find('пососеш') != -1:
                log(str(datetime.datetime.now())+" Функция - пососеш")
                i.send_text_message(user_nickname+", хто я?)))0)0")
                return True
            if i.uid == thread_id and (message_text.lower()).find('цаца ролл') == 0:
                random.seed()
                rand = random.randint(0,100)
                log(str(datetime.datetime.now())+" Функция - цаца ролл: "+str(rand))
                i.send_text_message(user_nickname+", твоё случайное число: "+str(rand))
                return True
            if i.uid == thread_id and (message_text.lower()).find('цаца ду ') == 0:
                #rand = random.randint(0,100)
                text_plus = message_text[8:len(message_text)]
                if random.randint(0,100) > 49:
                    log(str(datetime.datetime.now())+" Функция - цаца ду: успешно")
                    i.send_text_message("[I]"+text_plus+"[Успешно]")
                else:
                    log(str(datetime.datetime.now())+" Функция - цаца ду: неуспешно")
                    i.send_text_message("[I]"+text_plus+"[Неуспешно]")
                return True
            if i.uid == thread_id and (message_text.lower()).find('цаца дия ') == 0:
                #rand = random.randint(0,100)
                text_plus = message_text[9:len(message_text)]
                if random.randint(0,100) > 49:
                    log(str(datetime.datetime.now())+" Функция - цаца дия: успешно")
                    i.send_text_message("[I]"+user_nickname+" "+text_plus+"[Успешно]")
                else:
                    log(str(datetime.datetime.now())+" Функция - цаца дия: неуспешно")
                    i.send_text_message("[I]"+user_nickname+" "+text_plus+"[Неуспешно]")
                return True
            if i.uid == thread_id and (message_text.lower()).find('цаца ты кто') != -1:
                log(str(datetime.datetime.now())+" Функция - цаца ты кто")
                i.send_text_message(user_nickname+", я тебе ничего не расскажу, а вдруг ты нацик?")
                return True
            if i.uid == thread_id and (message_text.lower()).find('цаца') == 0:
                log(str(datetime.datetime.now())+" Функция - цаца")
                i.send_text_message(user_nickname+", не трогай мене, животне вонюче. Я вам не нанімалась -_-")
                return True
            if i.uid == thread_id and (message_text.lower()).find('стелла це машка') != -1:
                log(str(datetime.datetime.now())+" Функция - стелла це машка")
                i.send_text_message(user_nickname+", Абсолютно с тобой сагласна, гдє подпісивать?")
                return True

    def on_group_member_join(self, data):
        data = data['o']['chatMessage']
        user_id = data['author']['uid']
        user_nickname = data['author']['nickname']
        thread_id = data['threadId']
        #Если смс от бота, он не реагирует.
        if user_id == self.client.uid:
            return False
        for i in self.selected_chats:
            if i.uid == thread_id:
                i.send_text_message(self.hi18chat_text.replace('{name}', user_nickname))
                i.send_text_message(self.hi18chat2_text)
                i.send_text_message(self.hi18chat3_text)

#    def auto_sms(self, chat):
#        while True:
#            chat.send_text_message("huy sosi")
#            time.sleep(180)
