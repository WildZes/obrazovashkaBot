from handlers.handler import Handler
from settings import config
from tb_forms import BaseForm, fields


class HandlerSettings(Handler):

    def __init__(self, bot):
        super().__init__(bot)
        self.count_time = 300
        self.count_limit = 1000

    def handle(self):
        @self.bot.message_handler(func=lambda message: message.text == config.KEYBOARD['GROCERY'])
        def handle(message):
            self.tbf.send_form(message.chat.id, SetSettings())
            print('handlesend')

        @self.tbf.form_submit_event("SETINGS")
        def submit_register_update(call, form_data):
            try:
                self.count_time = int(form_data.count_time) * 60
                self.count_limit = int(form_data.count_limit)
                print('HStry')
            except ValueError:
                self.bot.send_message(call.message.chat.id,
                                      f'Оу, нужны подходящие значиния: время в минутах, лимит числовой... Начни заново \U0001F447',
                                      reply_markup=self.keyboards.start_menu())
                print('ye')
                return
            self.bot.send_message(call.message.chat.id,
                                  f'Сеттинги заапруфлены... \U0001F447',
                                  reply_markup=self.keyboards.start_menu())


class SetSettings(BaseForm):
    update_name = "SETINGS"
    form_title = "Понапридумывали:"
    count_time = fields.StrField("Время", error_message="Something wrong", default_value="300")
    count_limit = fields.StrField("Предел", "1000")
    freeze_mode = False
    close_form_but = True
    submit_button_text = "Подтвердить"