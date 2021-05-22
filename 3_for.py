"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
  school_scores = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [5, 3, 3, 3, 4, 5, 2, 3]},
    {'school_class': '4c', 'scores': [3, 4, 5]},
    {'school_class': '4d', 'scores': [5, 4, 3, 4, 5]},
  ]
  med_school = 0
  num_scores = 0
  for classes in school_scores:
    med_class = 0
    for i in classes['scores']:
      med_class += i
      med_school += i
    med_class = round(med_class / len(classes['scores']), 1)
    num_scores += len(classes['scores'])
    print(f"Средний балл по классу {classes['school_class']} = {med_class}")
  med_school = round(med_school / num_scores, 1)
  print(f"Средний балл по школе = {med_school}")
  
if __name__ == '__main__':
  main()
