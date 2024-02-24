from tb_forms import TelebotForms, BaseForm, fields
from telebot import TeleBot
from settings import config

token = config.TOKEN
bot = TeleBot(token)
tbf = TelebotForms(bot)


class TestRegisterForm(BaseForm):
    update_name = "submit_register_form"
    form_title = "TBF Test Register Form"
    name = fields.StrField("Name", "Enter your name:")
    group_number = fields.NumberField(
        "Group number", "Select your group number:", only_int=True, key_mode=True, input_range=(1, 10))
    sex = fields.ChooseField("Sex", "Select your sex:", answer_list=["male", "female"])
    date_of_birth = fields.DateTimeField("Date of Birth", "Select your date of birth: ",
                                         only_date=True, current_year_only=False, years_range=80)
    photo = fields.MediaField(
        "Photo", "Enter your photo:",
        valid_types=['photo'], required=False, error_message="Error. You can only send a photo")
    freeze_mode = True
    close_form_but = False
    submit_button_text = "Register"


@bot.message_handler(commands=['start'])
def start_update(message):
    tbf.send_form(message.chat.id, TestRegisterForm())


@tbf.form_submit_event("submit_register_form")
def submit_register_update(call, form_data):
    print(form_data)  # Completed form data
    bot.send_message(call.message.chat.id, "Successful registration")

bot.polling(none_stop=True)