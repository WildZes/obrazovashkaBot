import abc
from markup.markup import Keyboards
from tb_forms import TelebotForms


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot, p):

        self.bot = bot
        self.keyboards = Keyboards()
        self.tbf = TelebotForms(bot)
        self.p = p

    @abc.abstractmethod
    def handle(self):
        pass
