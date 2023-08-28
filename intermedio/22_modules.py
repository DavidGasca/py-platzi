import sys
print(sys.path)

import re #expresiones regulares
text = 'Mi número telefonico es: 6581111, el país es 52 y el número es 7'
print( re.findall('\w+', text) )
print( re.findall('[0-9]+', text) )

import time
timestamp = time.time()
print( timestamp )
print( f'local { time.asctime( time.localtime() ) }' )

import collections
num = [1, 2, 3, 1, 2, 4, 5, 1]
counter = collections.Counter( num )
print( counter )