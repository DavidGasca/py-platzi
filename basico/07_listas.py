lista = [1,2,3,4]
print(lista)
print(type(lista))

lista = ['hola', "mundo"]
print(lista)
print(type(lista))

lista = ['hola', "mundo", 1, 1.1, True]
print(lista)
print(type(lista))

lista[0] = 2
print(lista)

#lista[6] = 6  #error fuera de rango
#print(lista)

print(lista[1:3])
print(True in lista)
print(1.11 in lista)
print('hola' in lista)
print('mundo' in lista)

