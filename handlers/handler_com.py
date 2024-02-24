from handlers.handler import Handler


class HandlerCommands(Handler):

    def __init__(self, bot, p):
        super().__init__(bot, p)


    def pressed_btn_start(self, message):

        self.bot.send_message(message.chat.id,
                              f'Привет! Давай, менюху нажимай...',
                              reply_markup=self.keyboards.start_menu())

    def handle(self):

        @self.bot.message_handler(commands=['start'])
        def handle(message):
            if message.text == '/start':
                self.pressed_btn_start(message)
