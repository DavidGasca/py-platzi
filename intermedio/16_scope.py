price = 10 #global

def inc():
  price = 20 #contexto local
  price += 2
  print(price)
  return price

print(price)
print( inc() )