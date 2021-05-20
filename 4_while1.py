"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
  while True:
    question = input('Как дела? ')
    if question == 'Хорошо':
      print('Вот так-то! Пока!')
      break
    else:
      print('Может всё-таки хорошо? Давай попробуем ещё!')

    
if __name__ == "__main__":
  hello_user()
