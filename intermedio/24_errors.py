print('hola')

sum = lambda x, y: x + y + 1 
try:
  assert sum(2,2) == 4, '2+2 si es 4'  #si no se cumple manda un AssertionError
except Exception as err:
  print(f'Error Assert: {err}')

try:
  age = 10
  if age < 18:
    raise Exception('Solo mayores de edad')
except Exception as e:
  print(e)

def my_divide(a, b):
  try:
    result = a / b
  except ZeroDivisionError as e:
    result = 'No se puede dividir por 0'
    print(e)
  return result
    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0