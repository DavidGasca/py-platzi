import pkg
'''
from pkg.mod_1 import funct1, funct2
from pkg.mod_2 import funct3

print(funct1())
print(funct2())
print(funct3())

#print(funct4())
'''

print(pkg.var)
#para acceder de esta forma, ver linea 5 de __init__, alli se importan los paquetes
print(pkg.mod_2.funct4()) 