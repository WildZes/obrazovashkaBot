from basic_bot import BasicBot

class ReplierBot(BasicBot):
    def __init__(self, token):
        super().__init__(token)
        self.handler = {"message":self.reply, "inline_query":self.inline_query}