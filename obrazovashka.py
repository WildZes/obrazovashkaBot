from telebot import TeleBot, util
from settings import config
from handlers.handler_main import HandlerMain


class TelBot:

    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):

        self.token = config.TOKEN
        self.bot = TeleBot(self.token)
        self.handler = HandlerMain(self.bot)

    def start(self):

        self.handler.handle()

    def run_bot(self):

        self.start()
        self.bot.polling(none_stop=True, allowed_updates=util.update_types)


if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()
