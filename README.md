
# amino-bot  
Бот для мониторинга чатов амино. В дальнейшем планируется расширение функционала.

# Установка
Для корректной работы установите себе на компьютер git (https://git-scm.com/downloads)

Для успешной установки вам необходима версия Python 3.7+

1. Скачать архив их репозитория или клонировать его
2. Перейти в папку с проектом и открыть консоль
3. Установить зависимости `python -m pip install -r requirements.txt`
4. Запустить бота `python main.py`

# Настройка
Вы можете настроить сообщение при нарушении в файле `warning.txt`

*При запуске скрипта автоматически проверяется наличие обновлений*

Настроить автообновление вы можете в файле `config.py`

Буду очень благодарен, если вы будете предлагать какие-то доработки во владке `Issues`

# Телеграм бот
Есть возможность логирования в телеграм

Чтобы использовать эту функцию вам необходимо настроить соответсвующие переменные в файле `config.py`

После этого запустите скрипт для настройки бота `python config_bot.py`

Скрипт нужно запускать только один раз чтобы бот знал куда отправлять логи

-----------------------------
  
*P.S. Некоторую часть кода повзаимстовал у gastrodon*
