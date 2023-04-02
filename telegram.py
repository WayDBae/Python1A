import telebot
from telebot import types
bot = telebot.TeleBot("6239532031:AAFq_oaH2k-inga8L3pIGws6woRvC9f9yVs")
name = ""
surname = ""
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/reg":
        global name
        global surname
        global age
        name, surname, age = "", "", 0
        bot.send_message(message.chat.id,"Как вас зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.chat.id, "Напиши /reg")

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.chat.id, "Сколько вам лет?")
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.chat.id, "Цифрами, пожалуйста!")
    question = 'Тебе ' + str(age) + " лет, \n" "тебя зовут " + name + " " + surname + "?"
    bot.send_message(message.chat.id, question)
    
    keyboard = types.InlineKeyboardMarkup()
    py = types.InlineKeyboardButton(text = 'Python', callback_data='py')
    c = types.InlineKeyboardButton(text = 'C#', callback_data='c')
    java = types.InlineKeyboardButton(text = 'Java', callback_data='java')
    php = types.InlineKeyboardButton(text = 'PHP', callback_data='php')

    keyboard.add(py, c, java, php)
    question1 = "Какими языками программирования вы практикуетесь?"
    bot.send_message(message.chat.id, text = question1, reply_markup=keyboard)
    @bot.callback_query_handler(func = lambda call: True)
    def callback_worker(call):
        keyboard = types.InlineKeyboardMarkup()
        l_p = ["Python", "C#", "PHP","Java"]
        s = 1
        if call.data == 'py':
            l_p.pop(0)
        elif call.data == 'c':
            l_p.pop(1)
        elif call.data == 'php':
            l_p.pop(2)
        elif call.data == 'java':
            l_p.pop(3)
        for i in range(4):
            l_p[i] = types.KeyboardButton(text = l_p[i], callback_data=l_p[i])
            keyboard.add(l_p[i])
            s+=1
        question2 = "Какой язык программирования хотите освоить?"
        bot.send_message(call.message.chat.id, text = question2, reply_markup = keyboard)

bot.infinity_polling()
