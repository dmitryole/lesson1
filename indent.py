'''
import random
x = random.randint(1, 10)

def more_or_less(num):
    if x >= 5:
        print('Больше 5')
    else:
        print('Меньше 5')

more_or_less(x)
print(f'X = {x}')
'''
x = 0

while x < 10:
    print(x)
x = x + 1 #бесконечная упячка ctrl+c
