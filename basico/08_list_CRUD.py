'''
append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
'''
lista = [1, 2, 3, 4, 5]
lista[-1] = 10
print(lista)

lista.append(11)
print(lista)

lista.insert(1,1.1)
print(lista)

lista.insert(-1,12) #no toma en cuenta el negativo, lo inserta en la posicion 1
print(lista)

tasks = ['t1', 't2']
fusion = lista + tasks
print(fusion)

fusion[ fusion.index('t1') ] = 'T1'
print(fusion)

fusion.remove('T1')
print(fusion)

fusion.pop()
print(fusion)

fusion.pop( fusion.index(1.1) )
print(fusion)

fusion.reverse()
print(fusion)

fusion.sort()
print(fusion)
fusion.reverse()
print(fusion)

#fusion.append('a') #ya no es posible ordenar porque ya hay datos mezclados, error
fusion.append(1.1)
print(fusion)
fusion.sort() 
print(fusion)