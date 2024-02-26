from handlers.handler import Handler
from telebot.types import CallbackQuery
import base
import time


class HandlerInlineQuery(Handler):

    def __init__(self, bot, p):

        super().__init__(bot, p)

    def handle(self):

        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call: CallbackQuery):
            # code = call.data
            if 'TIME' in call.data:
                self.bot.delete_message(call.message.chat.id, call.message.id)
                self.bot.send_message(call.message.chat.id, "Время на решения",
                                      reply_markup=self.keyboards.min_choice())
            if 'LIMIT' in call.data:
                self.bot.delete_message(call.message.chat.id, call.message.id)
                self.bot.send_message(call.message.chat.id, "Выбери предел",
                                      reply_markup=self.keyboards.lim_choice())
            if '60' in call.data or '180' in call.data or '300' in call.data:
                self.bot.delete_message(call.message.chat.id, call.message.id)
                self.p.count_time = (int(call.data))
                self.bot.send_message(call.message.chat.id, 'Выбор сделан. Продолжишь?',
                                      parse_mode="HTML",
                                      disable_web_page_preview=True,
                                      reply_markup=self.keyboards.settings_menu())
            if call.data in ['10', '100', '200', '500', '1000']:
                self.bot.delete_message(call.message.chat.id, call.message.id)
                self.p.count_limit = (int(call.data))
                self.bot.send_message(call.message.chat.id, 'Выбор сделан. Продолжишь?',
                                      parse_mode="HTML",
                                      disable_web_page_preview=True,
                                      reply_markup=self.keyboards.settings_menu())
            if 'START' in call.data:
                base.c_down(self.bot, call.message, self.p.count_down)
                self.p.s_time = time.time()
                self.p.last_timer_id = self.bot.send_message(call.message.chat.id,
                                                             str(self.p.count_time) + " сек").message_id
                self.p.n1, self.p.n2 = base.make_sample(self.p.count_limit)
                self.p.eq_id = self.bot.send_message(call.message.chat.id, f'{self.p.n1} + {self.p.n2}').message_id
                self.p.equating = True
            if call.data == 'MAIN':
                self.bot.delete_message(call.message.chat.id, call.message.id)
                self.bot.delete_message(call.message.chat.id, self.keyboards.remove.message_id)
                self.number = 0
                self.bot.send_message(call.message.chat.id, "Начальное меню",
                                      reply_markup=self.keyboards.start_menu())




        # self.count_time = 300
        # self.count_limit = 1000
        # self.count_down = 3
        # self.eq_id, self.n1, self.n2 = None, None, None
        # self.equating = False
        # self.s_time = None