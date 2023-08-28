def get_population():
  keys = ['mex', 'per']
  values = [1222, 1111]
  return keys, values

var = 'hola'

def get_population_by_country(data, country):
  return list( filter(lambda item : item['country'] == country, data))