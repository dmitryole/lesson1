'''''
def discointrd(price, discount, max_discount = 20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Максимальная скидка не должна быть больше 100')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return(price_with_discount)
'''''
'''''
price_discointrd = discointrd(100, 5)
print(price_discointrd)

product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
product['with_discount'] = discointrd(product['price'],product['discount'])
print(product)
'''''
'''''
price_discointrd = discointrd(100, 5)
print(discointrd(100, 5))
print(discointrd(100, 50))
print(discointrd(100, 50, max_discount = 60))
'''''

#Задание1
def get_summ(one, two, delimiter='&'):
    return(f'{one}{delimiter}{two}')

summ = get_summ("Learn","python")
print(summ.upper())

#Задание2
def iformat_price(price):
    int(price)
    return(f'Цена: {price} руб')

print(iformat_price(56.24))
