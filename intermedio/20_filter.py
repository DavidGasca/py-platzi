numbers = [1, 2, 3, 4, 5, 6]
pares = list( filter(lambda x: x%2==0, numbers) )
print(numbers)
print(pares)

people = [
  {'name' : 'Pedro',    'country': 'Colombia',    'age' : 18,    'course' : 'developer'},
  {'name' : 'Juan',    'country': 'Perú',    'age' : 17,    'course' : 'UX'  },
  {'name' : 'Carlos',    'country': 'Chile',    'age' : 31,    'course' : 'Diseño'  },
  {'name' : 'Ana Maria',    'country': 'Colombia',    'age' : 25,    'course' : 'Tester'  }
]

#filter no altera el objeto original
countrie = list(filter(lambda pais: pais['country'] == 'Colombia', people))
print(countrie)
print(len(countrie))
print(people)
print(len(people))