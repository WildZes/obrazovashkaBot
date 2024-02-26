from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    InlineKeyboardMarkup, InlineKeyboardButton
from settings import config


class Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Keyboards(metaclass=Singleton):

    def __init__(self):

        self.markup = None
        self.remove = None

    def set_btn(self, name):

        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):

        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('START')
        itm_btn_2 = self.set_btn('SETTINGS')
        itm_btn_3 = self.set_btn('HELP')
        self.markup.row(itm_btn_1, itm_btn_2, itm_btn_3)
        return self.markup

    def settings_menu(self):

        self.markup = InlineKeyboardMarkup()
        itm_btn_1 = InlineKeyboardButton('Таймер', callback_data='TIME')
        itm_btn_2 = InlineKeyboardButton('Предел', callback_data='LIMIT')
        itm_btn_3 = InlineKeyboardButton(config.KEYBOARD['X'], callback_data='START')
        self.markup.row(itm_btn_1, itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):

        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('BACK_STEP')
        self.markup.row(itm_btn_1)
        return self.markup

    def restart_menu(self):

        self.markup = InlineKeyboardMarkup()
        self.markup.add(InlineKeyboardButton(config.KEYBOARD['START'], callback_data='START'))
        return self.markup

    def min_choice(self):

        self.markup = InlineKeyboardMarkup()
        itm_btn_1 = InlineKeyboardButton('1 мин.', callback_data='60')
        itm_btn_2 = InlineKeyboardButton('3 мин.', callback_data='180')
        itm_btn_3 = InlineKeyboardButton('5 мин.', callback_data='300')
        self.markup.row(itm_btn_1, itm_btn_2, itm_btn_3)
        return self.markup

    def lim_choice(self):

        self.markup = InlineKeyboardMarkup()
        itm_btn_1 = InlineKeyboardButton('100', callback_data='100')
        itm_btn_2 = InlineKeyboardButton('200', callback_data='200')
        itm_btn_3 = InlineKeyboardButton('500', callback_data='500')
        itm_btn_4 = InlineKeyboardButton('1000', callback_data='1000')
        itm_btn_5 = InlineKeyboardButton('10', callback_data='10')
        self.markup.row(itm_btn_5, itm_btn_1, itm_btn_2, itm_btn_3, itm_btn_4)
        return self.markup


    def remove_menu(self):

        return ReplyKeyboardRemove()
