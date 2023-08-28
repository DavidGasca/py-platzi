#transformación básica y a mano
numbers = [1, 2, 3, 4]
numV2 = []
for i in numbers:
  numV2.append(i*2)

print(numbers)
print(numV2)

#transfomacion de lista y es HOF, la funcion no se pude definir, solo lambda
numV3 = map(lambda i: i*2, numV2)
print( numV3 )
print( list( numV3) )

#ahora map sobre 2 listas, pero la transformación lo hace sobre la lista mas pequeña
numbersCont = [5, 6, 7]
res = list( map( lambda x, y : x + y, numbersCont, numbers ) )
print( res )

original = [1,2,3,4,5] 
new = []

for x in original:
	new.append(x * 2)

print(new)
new = list(map(lambda x: x * 2, original))
print(new)