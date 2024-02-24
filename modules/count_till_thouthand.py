from modules.basic_bot import BasicBot
import random


class CountBot(BasicBot):

    def __init__(self, token):
        super().__init__(token)
        self.num1 = 1000
        self.num2 = 1000
        self.handler = {"message": self.reply, "inline_query": self.inline_query}

    def reply(self, message):
        options = {"chat_id": message["chat"]["id"]}
        take_it = True
        if message["text"].startswith("/"):
            if message["text"].startswith("/start"):
                num1, num2 = self.make_sample()
                text = ("Привет.\n"
                        "Давай учиться считать.\n"
                        f"{num1}  +  {num2}")
                options["parse_mode"] = "HTML"
            elif message["text"].startswith("/stop"):
                text = "Ок, давай до свидания, но возвращайся еще."
            elif message["text"].startswith("/help"):
                text = "Все просто, я присылаю примеры, ты их решаешь. Когда устанешь пиши /stop"
            else:
                text = "Вообще не пон..."
                take_it = False
        else:
            text, take_it = self.answer_check(message["text"])

        options["text"] = text
        self.send_message(**options)

        return take_it

    def inline_query(self, query):
        result = {"type": "article",
                  "id": "std",
                  }

        text, take_it = self.answer_check(query["query"])
        result["title"] = text
        result["input_message_content"] = {"message_text": text}

        self.answer_inline_query(query, result)

        return take_it

    def answer_check(self, orig):
        try:
            if int(orig) == self.num1 + self.num2:
                self.num1, self.num2 = 1000, 1000
                num1, num2 = self.make_sample()
                text = ("Молодчина!\n"
                        "Давай еще.. (/stop для остановки)\n"
                        f"{num1}  +  {num2}")
            else:
                text = ("Неа(((\n"
                        "Попробуй снова (/stop для остановки)\n"
                        f"{self.num1}  +  {self.num2}")
        except:
            text = "Не пон..."

        return text, True

    def make_sample(self):
        while self.num1 + self.num2 > 1000:
            self.num1 = random.randint(1, 1000)
            self.num2 = random.randint(1, 1000)

        return self.num1, self.num2

# import  schedule
# from threading import Thread
# def schedule_checker():
#     while True:
#         schedule.run_pending()
#         sleep(1)
# ...
#     send = bot.send_message(message.chat.id,'Тевирп')
#     bot.register_next_step_handler(send,sending)
# def sending(message):
#    schedule.every(10).seconds.do(sch,message).tag(message.chat.id)
# def sch(message):
#     bot.send_message(message.chat.id,'Отправил сообщение через 10 сек')
#     schedule.clear(message.chat.id)
