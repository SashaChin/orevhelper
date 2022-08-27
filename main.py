import telebot
import random
from telebot import types
# Загружаем список курсов оверван
f = open('kursi.txt', 'r', encoding='UTF-8')
kursi = f.read().split('\n')
f.close()
# Загружаем список цен на курсы
f = open('cena.txt', 'r', encoding='UTF-8')
cena = f.read().split('\n')
f.close()
# Загружаем список контактов
f = open('kontakt.txt', 'r', encoding='UTF-8')
kontakt = f.read().split('\n')
f.close()
# Загружаем список места проведения курсов
f = open('mesto.txt', 'r', encoding='UTF-8')
mesto = f.read().split('\n')
f.close()
# Загружаем список новостей
f = open('novosti.txt', 'r', encoding='UTF-8')
novosti = f.read().split('\n')
f.close()
# Загружаем список акций
f = open('akcii.txt', 'r', encoding='UTF-8')
akcii = f.read().split('\n')
f.close()
# Загружаем список социальных сетей
f = open('soc.txt', 'r', encoding='UTF-8')
soc = f.read().split('\n')
f.close()
# Создаем бота
bot = telebot.TeleBot('5519835696:AAFlo0aqVqIiIYlS6DuCIvSFwjzTxAvQLXk')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем кнопки
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Список курсов")
        item2 = types.KeyboardButton("Цены")
        item3 = types.KeyboardButton("Контакты")
        item4 = types.KeyboardButton("Место проведение курсов")
        item5 = types.KeyboardButton("Актуальные новости")
        item6 = types.KeyboardButton("Акции")
        item7 = types.KeyboardButton("Социальные сети")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)
        bot.send_message(m.chat.id, 'Нажми: \nСписок курсов - что бы получить информацию актуальных курсов в школе OVERONE\nЦены - что бы получить актуальные цены на курсы\nКонтакты - что бы получить список наших контактов\nМесто - для получения мест проведений занятий\nАктуальные новости - новости OVERONE\nАкции - что бы получить актуальные скидки и акции на курсы\nСоциальные сети - подписывайтесь на наши соц. сети  ',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдает курсы оверван
    if message.text.strip() == 'Курсы':
            answer = kursi
    # Если юзер прислал 2, выдает список цен на курсы
    elif message.text.strip() == 'Список цен на курсы':
            answer = cena
    # Если юзер прислал 3, выдает контакты
    elif message.text.strip() == 'Контакты':
            answer = kontakt
    # Если юзер прислал 4, выдает место проведение курсов
    elif message.text.strip() == 'Место проедения курсов':
            answer = mesto
    # Если юзер прислал 5, выдает актуальные новости
    elif message.text.strip() == 'Актуальные новости':
            answer = novosti
    # Если юзер прислал 6, выдает акции и скидки
    elif message.text.strip() == 'Акции и скидки':
            answer = akcii
    # Если юзер прислал 7, выдает социальные сети
    elif message.text.strip() == 'Социальные сети':
            answer = soc
    # Отсылает отве бота
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)