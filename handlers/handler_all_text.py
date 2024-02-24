from handlers.handler import Handler
from settings.messages import MESSAGES
from settings import config
import base
import time


class HandlerAllText(Handler):

    def __init__(self, bot, p):

        super().__init__(bot, p)

    def pressed_btn_settings(self, message):

        self.bot.send_message(message.chat.id, 'Кликай настройку',
                              parse_mode="HTML",
                              disable_web_page_preview=True,
                              reply_markup=self.keyboards.settings_menu())

    def pressed_btn_info(self, message):

        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode="HTML",
                              disable_web_page_preview=True,
                              reply_markup=self.keyboards.info_menu())

    def pressed_btn_back(self, message):

        self.bot.send_message(message.chat.id, "Начальное меню",
                              reply_markup=self.keyboards.start_menu())

    def handle(self):

        @self.bot.message_handler(func=lambda message: True)
        def handle(message):

            if message.text == config.KEYBOARD['SETTINGS']:
                self.keyboards.remove_menu()
                self.pressed_btn_settings(message)
            if message.text == config.KEYBOARD['HELP']:
                self.pressed_btn_info(message)
            if message.text == config.KEYBOARD['BACK_STEP']:
                self.pressed_btn_back(message)
            if message.text == config.KEYBOARD['START']:
                self.keyboards.remove_menu()
                base.c_down(self.bot, message, self.p.count_down)
                self.p.s_time = time.time()
                self.p.last_timer_id = self.bot.send_message(message.chat.id, time.time() - self.p.s_time).message_id
                self.p.n1, self.p.n2 = base.make_sample(self.p.count_limit)
                self.p.eq_id = self.bot.send_message(message.chat.id, f'{self.p.n1} + {self.p.n2}').message_id
                self.p.equating = True
            if self.p.equating:
                if time.time() - self.p.s_time > self.p.count_time:
                    self.p.eq_id = None
                    self.p.equating = False
                    self.bot.delete_message(message.chat.id, self.p.last_timer_id)
                    self.bot.send_message(message.chat.id, 'Баста, карапузики...время вышло')
                    self.bot.send_message(message.chat.id, f'Зацени!\nПравильно: {self.p.correct}\nНеправильно: {self.p.incorrect} ')
                    self.p.last_timer_id = None
                    self.p.correct, self.p.incorrect = 0, 0
                else:
                    if self.p.last_timer_id:
                        self.bot.edit_message_text(round(time.time() - self.p.s_time), message.chat.id, self.p.last_timer_id)
            if self.p.eq_id and message.text != config.KEYBOARD['START']:
                t, r = base.answer_check(self.p.n1, self.p.n2, message.text)
                self.bot.delete_message(message.chat.id, self.p.eq_id)
                self.bot.send_message(message.chat.id, t)
                self.bot.delete_message(message.chat.id, self.p.last_timer_id)
                self.p.last_timer_id = self.bot.send_message(message.chat.id, round(time.time() - self.p.s_time)).message_id
                self.p.n1, self.p.n2 = base.make_sample(self.p.count_limit)
                self.p.eq_id = self.bot.send_message(message.chat.id, f'{self.p.n1} + {self.p.n2}').message_id
                if r:
                    self.p.correct += 1
                else:
                    self.p.incorrect += 1
