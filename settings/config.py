import os
from emoji import emojize
from dotenv import load_dotenv

load_dotenv(".env")
TOKEN = os.getenv('token')
VERSION = '0.0.2'
AUTHOR = ' @wildzes'

KEYBOARD = {
    'TIME': emojize(':timer_clock: Время'),
    'START': emojize(':nut_and_bolt: Тренироваться!'),
    'SETTINGS': emojize(':megaphone: Свои правила.'),
    'HELP': emojize(':magnifying_glass_tilted_right: Помогатор'),
    'BACK_STEP': emojize('◀️'),
    'LIMIT': emojize(':bullseye: "БЕС"предел'),
    'X': emojize(':racing_car: Погнали'),
    'COPY': '©️'
}
