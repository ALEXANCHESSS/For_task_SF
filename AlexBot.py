import telebot
from extension import ConvertationException, Converter
from config import TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты>' \
           '<в какую валюту перевести><количество переводимой валюты>' \
           'Для просмотра доступных валют введите /value'
    bot.reply_to(message, text)

@bot.message_handler(commands='value')
def value(massage):
    text = 'Доступные валюты'
    for i in keys.keys():
        text = '\n'.join((text, i))
    bot.reply_to(massage, text)

@bot.message_handler(content_types='text')
def convert(message):
    try:
        list_convert = message.text.split(' ')

        if len(list_convert) != 3:
            raise ConvertationException('Введите ровно 3 переменные.')

        base, quote, amount = list_convert
        total = Converter.get_price(base, quote, amount)

    except ConvertationException as e:
        bot.reply_to(message, f'Ошибка ввода \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'Цена {amount} {base} в {quote} составляет {round((float(amount)) * total), 2}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
