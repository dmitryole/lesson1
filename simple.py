#Практика: Числа1

a = 2
b = 0.5
print(a + b)

#Практика: Строки1

name = 'Дмитрий'
print(f'Привет, {name}!')

#Практика: Числа2

v = int(input('Введите число от 1 до 10: '))
print(v+10)

#Практика: Строки2

name = input('Введите ваше имя: ')
print(f'Привет, {name.upper()}! Как дела?')

#Практика: Приведение типов
'''
float('1')
int('2.5')
bool(1)
bool('')
bool(0)
'''
print ('float("1") =',float('1'),'\nbool(1) =',bool(1),'\nbool("")=',bool(''),'\nbool(0) =',bool(0))
#print (int('2.5'))  #ValueError: invalid literal for int() with base 10: '2.5' 
print ('float("2.5") =',int(float('2.5')))
