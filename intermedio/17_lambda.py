#funcion normal
def inc(x):
  return x + 1

inc2 = lambda x : x + 1
res = inc2(10)
print(res)

full = lambda name, lastN: f'full: {name.title()} {lastN.title()}'
print( full('david','gasca') )

def high_ord_funct(x, funct):
  return x + funct(x)

res = high_ord_funct( 2, inc )
print( res )

high_ord_funct_lambda = lambda y, func: y * func(y)
res = high_ord_funct_lambda(2, inc)
print( res )

res = high_ord_funct_lambda(3, lambda x: x * 3)
print( res )