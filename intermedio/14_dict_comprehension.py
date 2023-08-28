import random

dict = {}
for i in range (1,5):
  dict[i] = i * 2

print(dict)

dict2 = { f'k{i}' : i*2 for i in range(1,5)}
print(dict2)

dict2 = { f'k{i}' : f'v-{i*2}' for i in range(1,5)}
print(dict2)

countries = ['mex', 'col', 'arg', 'bra', 'per']
population = {country: random.randint(1,10) for country in countries}
print( f'dict: {population}' )
print( f'items: {population.items()}' )

res = { country: pop for (country, pop) in population.items() if pop > 5 }
print(res)

keys = ['a', 'b', 'c']
values = [10, 20, 30, 40]

print( list( zip(keys, values) ))

nDict = { k:v for (k, v) in zip( keys, values) }
print( nDict )

text = 'Hola, aqui David'
unique = { c:text.count(c) for c in text if c in 'aeiou' }
print( unique )