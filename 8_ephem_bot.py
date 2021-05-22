"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem


import logging
import warnings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text.split()
    if user_text[0] == "/planet":
      planet_x = getattr(ephem, user_text[1])(date.today())
      if planet_x is not None:
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        text = ephem.constellation(planet_x)
        print(text)
        update.message.reply_text(text)
      else:
        text = user_text[1]
        print(f'Я не знаю планеты {text}. Проверьте правильность написания, а может ее просто нет в моей библиотеке.')
        update.message.reply_text(text)
    else:
      user_text = update.message.text 
      print(user_text)
      update.message.reply_text('Давай лучше про планеты?')
      

def main():
    mybot = Updater("1872034254:AAGKysT91wp9k8iOwTQ5nqKDbBLX2bVMul8", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
  main()
