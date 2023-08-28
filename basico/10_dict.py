dict = {
  'id':1,
  'name': 'david',
  'age': 40,
  'arr' : [1,2,3]
}

print(dict)
print(len(dict) )

print( dict['age'] )
print( dict.get('age') )
print( dict.get('age--') ) #maneja el error cuando no existe la llave

print( 'nollave' in dict )
print( 'id' in dict )

print( dict.setdefault('hola','adios') )
print(dict)

dict['arr'].append(4)
print( dict )

del dict['age']  #ambos esperan llave valida
dict.pop('name') #ambos esperan llave valida
print( dict )

print( dict.items() )
print( dict.keys() )
print( dict.values() )

x = ('key1', 'key2', 'key3')
y = [1, 2]
thisdict = dict.fromkeys(x, y)
print(thisdict)