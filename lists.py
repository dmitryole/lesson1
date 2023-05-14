'''
phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11"]
print('phones =',phones)
print('len(phones) =', len(phones))

phones.append("iPhone 12")
print('new phones =',phones)

print ('count iPhone 12 =', phones.count("iPhone 12"))
print ('count iPhone 9 =',phones.count("iPhone 9"))
print ('1 phones =',phones[1])
print ('-2 phones =',phones[-2])
print ('0-2 phones =',phones[0:2])
print ('n-3 phones =',phones[:3])
print ('3-n phones =',phones[3:])
print ('index Xiaomi Mi11 =',phones.index('Xiaomi Mi11'))

phones.sort()
print ('new index Xiaomi Mi11 =',phones.index('Xiaomi Mi11'))
print('sort phones =',phones)

print("Samsung Galaxy S21" in phones)

del phones[1]
print('new phones =',phones)
phones.remove ("iPhone 12")
print('new phones =',phones)
'''
numbers = [3, 5, 7, 9, 10.5]
print('numbers =',numbers)
numbers.append("Python")
print('len(numbers) =', len(numbers))
print ('0 numbers =',numbers[0])
print ('end numbers =',numbers[-1])
print ('2-4 numbers =',numbers[2:5])
numbers.remove ("Python")
