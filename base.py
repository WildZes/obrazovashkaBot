import time
import random


def c_down(bot, message, n):

    while n >= 0:
        msg_id = bot.send_message(message.chat.id, n).message_id
        time.sleep(1)
        bot.delete_message(message.chat.id, msg_id)
        n -= 1


def make_sample(limit):

    num1 = random.randint(1, limit)
    num2 = random.randint(1, limit)
    while num1 + num2 > limit:
        num1 = random.randint(1, limit)
        num2 = random.randint(1, limit)

    return num1, num2


def answer_check(first, second, answ):

    try:
        if int(answ) == first + second:
            return f'{first} + {second} = {answ}', True
    except ValueError:
        text = "Не пон..."
        return text, False
    return f'{first} + {second} \u2260 {answ}', False

