import telebot

import conf

from bs4 import BeautifulSoup

from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

bot = telebot.TeleBot(conf.TOKEN)


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    img = open('C:/Users/sergey/PycharmProjects/pythonProject2/telegram/static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, img)
    bot.reply_to(message,
                 f"Привет, сейчас я предложу выбрать дату поездки. Для этого НАПИШИ /date, "
                 f"{message.from_user.first_name}")


@bot.message_handler(commands=['date'])
def start(m):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(m.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"Ты выбрал {result}, теперь пора выбрать наш маршрут НАПИШИ /city ",
                              c.message.chat.id,
                              c.message.message_id)


start_city = ''
end_city = ''


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/city':
        bot.send_message(message.from_user.id, "Откда поедем?")
        bot.register_next_step_handler(message, get_start)
    else:
        bot.send_message(message.from_user.id, 'Напиши /city')


def get_start(message):
    global start_city
    start_city = message.text
    bot.send_message(message.from_user.id, 'Куда едем?')
    bot.register_next_step_handler(message, get_end)


def get_end(message):
    global end_city
    end_city = message.text
    bot.send_message(message.from_user.id, 'С ' + start_city + ' до ' + end_city)


# result
# start_city
# end_city   переменные


if __name__ == '__main__':
    bot.polling(none_stop=True)
