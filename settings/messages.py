from .config import KEYBOARD, VERSION, AUTHOR
from emoji import emojize

settings = """
<b>Помогатор.</b>

-<b>({}) - </b><i>Будешь решать примеры</i>
-<b>({}) - </b><i>Тоже будешь решать, но после настроек</i>
-<b>({}) - </b><i>Выбирай время и предел для примеров</i>
-<b>({}) - </b><i>Уже понял, чё это?</i>

<i>Ни о чём:</i>
-<b>версия программы: </b><i>{}</i>
-<b>разработчик: </b><i>{}</i>


""".format(
    emojize(':nut_and_bolt:'),
    emojize('❌'),
    emojize(':megaphone:'),
    emojize(':magnifying_glass_tilted_right:'),
    VERSION,
    KEYBOARD['COPY']+AUTHOR,
)

MESSAGES = {
    'settings': settings
}
