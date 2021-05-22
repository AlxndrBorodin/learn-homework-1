"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
  try:
    while True:
      question = input('Как дела? ')
      if question == 'Хорошо':
        print('Вот так-то! Пока!')
        break
      else:
        print('Может всё-таки хорошо? Давай попробуем ещё!')
  except KeyboardInterrupt:
    print('Пока!')
       

if __name__ == "__main__":
  hello_user()
