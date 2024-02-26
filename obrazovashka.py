from telebot import TeleBot, util
from settings import config
from handlers.handler_main import HandlerMain
import threading
import sys


class TelBot:

    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):

        self.token = config.TOKEN
        self.bot = TeleBot(self.token)
        self.handler = HandlerMain(self.bot)
        sys.path.append(r'C:\Users\user\PycharmProjects\obrazovashka\venv\jython-standalone-2.7.3.jar')

    def start(self):

        self.handler.handle()

    def run_bot(self):

        self.start()
        threading.Thread(target=self.bot.polling(none_stop=True, allowed_updates=util.update_types),
                         name='obrazovashkaBot', daemon=True).start()


if __name__ == '__main__':
    bot = TelBot()
    while True:
        bot.run_bot()
