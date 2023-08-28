
for el in range(5,10,2):
  print(el)

fruits = ["banana", "apple", "wathermelon"]
for el in fruits:
  print(el)

fruits = ("banana_T", "apple_T", "wathermelon_T")
for el in fruits:
  print(el)

product = {
    'name':'tshirt',
    'stock':10
  }
for el in product:
  print(el)

for el in product:
  print( el, ":", product[el] )

for key, value in product.items():
  print(key, ":>", value)

people = [
  {'name':'Juan', 'age':20},
  {'name':'Pedro', 'age':23},
  {'name':'Maria', 'age':22},
  {'name':'Pancho', 'age':25}
]

for person in people:
  print(person['name'])

primos = [2, 3, 5, 7, 11, 13, 17, 19]
print( primos[3] )