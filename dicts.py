from pprint import pprint  # визуально форматирует вывод
'''
product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1,
    "country": "US"
}
print (len(product))
product['memory'] = 256
print (product)
product['name'] = "iPhone 13"
print (product['price'])
print(product.get("country", "CN"))
del product['stock']
print (product)

phones = ["iPhone 12 Pro", "Samsung Galaxy S21", "Xiaomi Mi11"]
product ["recomended"] = phones
pprint (product)
#pprint (product["recomended"][0])
product ["recomended"].append('iPhone 9')
pprint (product)
'''
'''
stock = [
    {"name": "iPhone 12 Plus", "stock": 24, "price": 65432.1,
        "recomended": ["Samsung Galaxy S21", "iPhone 12"]},
    {"name": "Samsung Galaxy S21", "stock": 8,
        "price": 50000.0, "discount": 5000},
    {"name": "Xiaomi Mi11", "stock": 42, "price": 38000.5}]
pprint (stock[0]['recomended'][0])
stock[0]['recomended'].append('Xiaomi Mi11')
stock[2]['price'] = stock[2]['price'] - 30000
pprint (stock)

print(type(stock))
print(type(stock[0]))
print(type(stock[0]['recomended']))
'''
#Задание
weathers = {"city": "Москва", "temperature": "20"}
print (weathers['city'])
weathers['temperature'] = str(int(weathers['temperature']) - 5)
pprint (weathers)
print(weathers.get('country','Россия'))
weathers ["date"] = '27.05.2019'
print(len(weathers))