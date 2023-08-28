def suma(min, max):
  sum = 0
  for i in range(min, max):
    sum += i
  return sum

print( suma(1,10) )

#llamado con valores por defecto y se puede pasar 0 o todos los valores
#cuando se hace de esta forma
def volume(length = 1, width = 1, depth = 1):
  return 'volumen', length * width * depth

regreso = volume(width=2)
print( f'return en tupla {regreso}'  )

text, vol = volume(width=2)
print( f'return por valor text:{text} y vol:{vol}'  )