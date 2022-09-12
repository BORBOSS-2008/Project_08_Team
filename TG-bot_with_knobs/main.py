# import pandas
import telebot
import random
from telebot import types
# Загружаем список интересных фактов
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список поговорок
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()
# Создаем бота
bot = telebot.TeleBot('5786802967:AAFArKDT_tUEVMEfQLRWf_hWycfmL6gNpBc')
# Команда start

@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Поговорка")
        markup.add(item1)
        markup.add(item2)

        item3 = types.KeyboardButton("Говно")
        item4 = types.KeyboardButton("Параша")
        markup.add(item3)
        markup.add(item4)

        item5 = types.KeyboardButton("Школа")
        item6 = types.KeyboardButton("Работа")
        markup.add(item5)
        markup.add(item6)

        bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',  reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])

def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт

    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Поговорка':
        answer = random.choice(thinks)
    elif message.text.strip() == 'Факт':
        answer = random.choice(facts)
    elif message.text.strip() == 'Поговорка':
        answer = random.choice(thinks)
    elif message.text.strip() == 'Говно':
        answer = "Сам ты говно!"
    elif message.text.strip() == 'Параша':
        answer = "Это твой МОЗГ!!!"
    elif message.text.strip() == 'Школа':
        answer = "Ненавижу эту тюрьму для детей!"
    elif message.text.strip() == 'Работа':
        answer = "Там тоже плохо, но работаешь за ДЕНЬГИ..."
    elif message.text.strip() == 'Ароша':
        answer = "Орущая тварь, и очень весёлая ^.^"
    else:
        answer = ("Invalid Input. Try again!")


    bot.send_message(message.chat.id, answer)
        # bot.send_message(message.chat.id, "./start")

# Запускаем бота


bot.polling(none_stop=True, interval=0)


# bot.polling(none_stop=True, interval=0)




# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
