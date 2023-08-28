setA = {'mex','col','arg'}
setB = {'mex','bra','per'}

setC = setA.union(setB)
print( setC )
print( setA | setB ) #caracter de union

print( setA.intersection(setB) )
print( setA & setB )

print( setA.difference(setB) )
print( setB.difference(setA) )
print( setA - setB )

print( setA.symmetric_difference(setB) )
print( setB.symmetric_difference(setA) )
print( setA ^ setB )