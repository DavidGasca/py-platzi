for i in range(1,5):
  print(i)

my_iter = iter( range(1,5) )
print(my_iter)

print( next(my_iter) )
print( next(my_iter) )
print( next(my_iter) )
print( next(my_iter) )
#detencion de la iteracion, habría que controlarlo para evitar un "StopIteration"
#print( next(my_iter) ) 
