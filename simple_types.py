#1.Целые числа
'''
a = 2
b = 5
c = a - b
print(c)
'''
#2.Вещественные числа
'''
a = 2.5
b = 0.5
c = a - b
print(c)
'''
#3.Логический тип
'''
a = 2
b = 2.0
c = a == b
print(c)
'''
#4.Строки
'''
a = 'Привет'
b = 'мир'
#c = a + ' ' + b + '!' # суммирование строк
d = 2
c = f'{a} {b} {d}!' # f-строка
print(len (c)) # len() - длина строки
print(c.upper()) # upper() - верхний регистр
print(c.lower()) # upper() - нижний регистр
print(b.capitalize()) # capitalize() - заглавная буква
'''
'''
a = '  Привет  '
print(a.strip()) # strip() - убирание пробелов
a = 'Прив3т т3б3'.replace('3', 'e') # replace() - замена символа
print(a)
'''
'''
a = 'ПриветЫ'.lower().replace('ы', '').capitalize()
print(a)
a = 'Привет миры!'.replace('мир', 'python')
print(a)
a = 'learn.python.ru'
print(a.split('.')) split()# Разбиение строки в список
a = "Предложение из нескольких слов"
print(len(a.split())) # 4
'''
#4.None
'''
a = None
b = 0
c = 2.0
d = '2.0'
print (b is None)
print ('type(a)=',type(a),'\ntype(b)=', type(b),'\ntype(c)=', type(c),'\ntype(d)=', type(b),)
'''
#5.Ввод от пользователя
year = input('Введите год рождения: ')
real_age = 2023 - int(year)
print(f'Ваш возвраст: {real_age}')

