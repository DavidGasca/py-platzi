num = []
for el in range(1, 11):
  num.append(el * 2)

print(num)

numV2 = [ (el * 2) for el in range(10, 20)]
print( numV2 )

#primero hace el rango y va preguntando por el valor, luego saca e dato y multiplica
numV2 = [ (el * 2) for el in range(10, 20) if el % 2 == 0]
print( numV2 )

