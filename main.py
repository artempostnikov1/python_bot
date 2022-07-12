import telebot
from datetime import date
import io
import os

propusk = False
bot = telebot.TeleBot('#')

@bot.message_handler(commands=["start"])
def instruction(message):
    global propusk
    with io.open('uid.txt', encoding='utf-8') as file:
        for line in file:
            if message.from_user.username in line:
                propusk = True
    if (propusk):
        keybord = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_ofice = telebot.types.KeyboardButton("Офис")
        button_VED = telebot.types.KeyboardButton("ВЭД")
        button_factory = telebot.types.KeyboardButton("Производство")
        button_general = telebot.types.KeyboardButton("Общее")
        keybord.add(button_ofice, button_VED, button_factory, button_general)
        bot.send_message(message.chat.id, "Привет, я - бот. ", reply_markup=keybord)
    else: 
        bot.send_message(message.chat.id, "Нет доступа", reply_markup=telebot.types.ReplyKeyboardRemove())
    

def search_pasport(message):
    path = str(message.text) + ".pdf"
    cur_dir = os.getcwd()  # Dir from where search starts can be replaced with any path
    file_list = os.listdir(cur_dir + "/passports") #список файлов и директорий с заданным путем path
    check = True
    for name in file_list:
        if (name == path):
            bot.send_document(message.chat.id, open("passports/" + path, 'rb'))
            check = False
    if (check):
        bot.send_message(message.chat.id, "Не найдено", reply_markup=telebot.types.ReplyKeyboardRemove())
    instruction(message)


def search_covid(message):
    path = str(message.text) + ".pdf"
    cur_dir = os.getcwd()  # Dir from where search starts can be replaced with any path
    file_list = os.listdir(cur_dir + "/covid") #список файлов и директорий с заданным путем path
    check = True
    for name in file_list:
        if (name == path):
            bot.send_document(message.chat.id, open("covid/" + path, 'rb'))  
            check = False
    if (check):
        bot.send_message(message.chat.id, "Не найдено", reply_markup=telebot.types.ReplyKeyboardRemove())
    instruction(message)

def search_pilot(message):
    path = str(message.text) + ".pdf"
    cur_dir = os.getcwd()  # Dir from where search starts can be replaced with any path
    file_list = os.listdir(cur_dir + "/pilot") #список файлов и директорий с заданным путем path
    check = True
    for name in file_list:
        if (name == path):
            bot.send_document(message.chat.id, open("pilot/" + path, 'rb'))
            check = False
    if (check):
        bot.send_message(message.chat.id, "Не найдено", reply_markup=telebot.types.ReplyKeyboardRemove())
    instruction(message)

def factory(message):
    if(message.text == "Ссылки"):
        keybord = telebot.types.InlineKeyboardMarkup(row_width=1)
        button_uchet = telebot.types.InlineKeyboardButton(text="Учёт дронов", url="https://www.geoscan.aero/ru")
        button_sklad_uchet = telebot.types.InlineKeyboardButton(text="Складской учёт", url="https://www.geoscan.aero/ru")
        button_otchet_pilots = telebot.types.InlineKeyboardButton(text="Отчёты пилотов", url="https://www.geoscan.aero/ru")
        button_photo_for_send = telebot.types.InlineKeyboardButton(text="Фото для отправки", url="https://disk.yandex.ru/client/disk/Drone%20Show")
        button_db = telebot.types.InlineKeyboardButton(text="База данных", url="https://www.geoscan.aero/ru")
        button_timing_sborka = telebot.types.InlineKeyboardButton(text="Тайминги сборки", url="https://www.geoscan.aero/ru")
        button_registr = telebot.types.InlineKeyboardButton(text="Регистрация дронов РФ", url="https://www.geoscan.aero/ru")
        button_redien = telebot.types.InlineKeyboardButton(text="Redmine", url="https://redmine.corp.geoscan.aero/login?back_url=http%3A%2F%2F127.0.0.1%3A3000%2F")
        button_synology = telebot.types.InlineKeyboardButton(text="Synology", url="https://drive.corp.geoscan.aero/")
        button_yandex = telebot.types.InlineKeyboardButton(text="Я.Диск", url="https://disk.yandex.ru/client/disk/Drone%20Show")
        keybord.add(button_uchet, button_sklad_uchet, button_otchet_pilots, button_photo_for_send, button_db, button_timing_sborka, button_registr, button_redien, button_synology, button_yandex)
        sent = bot.send_message(message.chat.id, "ловите",
                         reply_markup=keybord)
        instruction(message)
    #if(message.text == "Документы"):


@bot.message_handler(content_types=['text'])
def dialog_one(message):
    global propusk
    if(message.text == "Меню" and propusk):
        keybord = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_ofice = telebot.types.KeyboardButton("Офис")
        button_VED = telebot.types.KeyboardButton("ВЭД")
        button_factory = telebot.types.KeyboardButton("Производство")
        button_general = telebot.types.KeyboardButton("Общее")
        keybord.add(button_ofice, button_VED, button_factory, button_general)
        sent = bot.send_message(message.chat.id, "Что?",
                         reply_markup=keybord)
        #bot.register_next_step_handler(sent, menu)

    if (message.text == "Офис" and propusk):
        keybord = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_links = telebot.types.KeyboardButton("Ссылки")
        button_docs = telebot.types.KeyboardButton("Документы")
        keybord.add(button_links, button_docs)
        sent = bot.send_message(message.chat.id, "Что?",
                         reply_markup=keybord)

    if (message.text == "Ссылки" and propusk):
        keybord = telebot.types.InlineKeyboardMarkup(row_width=1)
        button_projects = telebot.types.InlineKeyboardButton(text="Проекты/планы", url="https://www.geoscan.aero/ru")
        button_budj = telebot.types.InlineKeyboardButton(text="Бюджеты", url="https://www.geoscan.aero/ru")
        button_cer = telebot.types.InlineKeyboardButton(text="Cerebro", url="https://www.geoscan.aero/ru")
        button_nakl = telebot.types.InlineKeyboardButton(text="Накладные", url="https://www.geoscan.aero/ru")
        button_1c = telebot.types.InlineKeyboardButton(text="1С", url="https://www.geoscan.aero/ru")
        button_smart = telebot.types.InlineKeyboardButton(text="Smartway", url="https://www.geoscan.aero/ru")
        keybord.add(button_projects, button_budj, button_cer, button_nakl, button_1c, button_smart)
        sent = bot.send_message(message.chat.id, "ловите",
                         reply_markup=keybord)
        instruction(message)


    if (message.text == "Документы" and propusk):
        keybord = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        button_pass = telebot.types.KeyboardButton("Паспорта")
        button_covid = telebot.types.KeyboardButton("Сертификаты Covid")
        button_pilot = telebot.types.KeyboardButton("Сертифиаты пилотов")
        keybord.add(button_pass, button_covid, button_pilot)
        sent = bot.send_message(message.chat.id, "какие?",
                         reply_markup=keybord)

    if (message.text == "Паспорта" and propusk):
        sent = bot.send_message(message.chat.id, "чей?", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(sent, search_pasport)
    
    if (message.text == "Сертификаты Covid" and propusk):
        sent = bot.send_message(message.chat.id, "чей?", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(sent, search_covid)

    if (message.text == "Сертифиаты пилотов" and propusk):
        sent = bot.send_message(message.chat.id, "чей?", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(sent, search_pilot)

    if (message.text == "Общее" and propusk):
        #sent = bot.send_message(message.chat.id, "что желаете?", reply_markup=telebot.types.ReplyKeyboardRemove())
        keybord = telebot.types.InlineKeyboardMarkup(row_width=1)
        url_of_site = telebot.types.InlineKeyboardButton(text="Официальный сайт", url="https://www.geoscan.aero/ru")
        url_corp = telebot.types.InlineKeyboardButton(text="Корпоративный портал", url="https://example.com")
        url_synology = telebot.types.InlineKeyboardButton(text="Synology", url="https://drive.corp.geoscan.aero/")
        url_yandex = telebot.types.InlineKeyboardButton(text="Яндекс диск", url="https://disk.yandex.ru/client/disk/Drone%20Show")
        url_redmine = telebot.types.InlineKeyboardButton(text="Redmine", url="https://redmine.corp.geoscan.aero/login?back_url=http%3A%2F%2F127.0.0.1%3A3000%2F")
        url_photo = telebot.types.InlineKeyboardButton(text="Фото для отправки", url="https://disk.yandex.ru/client/disk/Drone%20Show")
        keybord.add(url_of_site, url_corp, url_synology, url_yandex, url_redmine, url_photo)
        sent = bot.send_message(message.chat.id, "ловите",
                         reply_markup=keybord)
        instruction(message)


    if(message.text == "Производство" and propusk):
        keybord = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_links = telebot.types.KeyboardButton("Ссылки")
        button_docs = telebot.types.KeyboardButton("Документы")
        keybord.add(button_links, button_docs)
        sent = bot.send_message(message.chat.id, "хули?",
                         reply_markup=keybord)
        bot.register_next_step_handler(sent, factory)

if __name__ == '__main__':
    bot.infinity_polling()