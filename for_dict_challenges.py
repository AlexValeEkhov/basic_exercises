# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# Решение
counter = {}
print('Задание 1:')
from collections import Counter
list = []
for student in students:
    list.append(student['first_name'])
counter = Counter(list)
for name in counter:
    print(f'{name}: {counter[name]}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# Решение
print('\nЗадание 2:')
list = []
counter = {}
for student in students:
    list.append(student['first_name'])     
  
counter = Counter(list)

c = 0
most_freq = ''
for name, count in counter.items():
    if count > c:
        c = count
        most_freq = name

print(f'Самое частое имя среди учеников: {most_freq}')
    

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# Решение

print('\nЗадание 3:')
class_number = 0
for clas in school_students:
    list = []
    class_number += 1
    for student in clas:
        list.append(student['first_name'])     
    
    counter = Counter(list)
    
    c = 0
    most_freq = ''
    for name, count in counter.items():
        if count > c:
            c = count
            most_freq = name
    print(f'Самое частое имя среди учеников в классе {class_number}: {most_freq}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]}, # Исправил класс повтор 2б на 2в.
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# Решение
print('\nЗадание 4:')
for clas in school:
    male = 0
    female = 0
    gender = bool
    for name in clas['students']:
        if name['first_name'] in is_male:
            gender = is_male[name['first_name'] ]
            if gender == True:
                male += 1
            else:
                female += 1
    print(f"Класс {clas['class']}: девочки {female}, мальчики {male}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# Решение
print('\nЗадание 5:')
for clas in school:
    male = 0
    female = 0
    gender = bool
    gender_most = ""
    for name in clas['students']:
        if name['first_name'] in is_male:
            gender = is_male[name['first_name'] ]
            if gender == True:
                male += 1
            else:
                female += 1
    if male > female:
        gender_most = "мальчиков"
    else:
        gender_most = "девочек"
    print(f"В классе {clas['class']} больше всего {gender_most}.")