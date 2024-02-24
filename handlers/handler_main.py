from handlers.handler_com import HandlerCommands
from handlers.handler_all_text import HandlerAllText
from handlers.handler_inline_query import HandlerInlineQuery
from settings.param import Param as p
# from handlers.handler_settings import HandlerSettings
# from handlers.handler_photo import HandlerForm


class HandlerMain:

    def __init__(self, bot):

        self.bot = bot
        self.p = p()
        self.handler_commands = HandlerCommands(self.bot, self.p)
        self.handler_all_text = HandlerAllText(self.bot, self.p)
        self.handler_inline_query = HandlerInlineQuery(self.bot, self.p)
        # self.handler_settings = HandlerSettings(self.bot)
        # self.handler_photo = HandlerForm(self.bot)

    def handle(self):

        self.handler_commands.handle()
        self.handler_all_text.handle()
        self.handler_inline_query.handle()
        # self.handler_settings.handle()
        # self.handler_photo.handle()
