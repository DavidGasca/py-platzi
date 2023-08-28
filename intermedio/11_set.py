set_countries = {'mx','col','per'}
print( set_countries )
print( type(set_countries) )

set_countries = {'mx','col','per', 'MX', 1, 2, 2, 3}
print( set_countries )

set_from_string = set('hoola')  #ojo esta quitando los duplicados
print( set_from_string )

set_from_tuple = set( ('abc', 'abe', 'abf', 'abc') )
print( set_from_tuple )

set_from_list = set( ['abc', 'abe', 'abf', 'abc'] )
print( set_from_list )

uniques = list(set_from_list)
print(uniques)
'''
add(): Añade un elemento.
update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
discard(): Elimina un elemento y si ya existe no lanza ningún error.
remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
clear(): Elimina todo el contenido del conjunto.
'''
print( len(set_countries) )
print( 'mx' in set_countries )
set_countries.add('br')
print( set_countries )

set_countries.update({'arg','br','ecu'})
print( set_countries )

set_countries.discard(1)
print( set_countries )
set_countries.discard(3)
print( set_countries )
set_countries.discard(10)
print( set_countries )

set_countries.remove(2)
print( set_countries )
#set_countries.remove(2) #exeption if not exists
#print( set_countries )

print( set_countries.pop() )
print( set_countries )

set_countries.clear()
print( set_countries )