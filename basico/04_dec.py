x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

print( x == y)

#con base en cadenas
y_str = format(y, ".2g")
print(y_str)
print( y_str == str(x) )
print( x == float(y_str) )

print("*" * 20)
#ahora con base matematica
#tolerancia = 0.000000000000001  #true, aun es tolerable el error
tolerancia = 0.0000000000000001  #false, es demasiada la tolerancia
print( abs( x - y ) )
print( abs( x - y ) < tolerancia )
