import mod

countries = [
  {'country':'mex', 'population':100},
  {'country':'col', 'population':200},
  {'country':'bol', 'population':300},
  {'country':'bra', 'population':400},
]

print(__name__, 'main.py')

def run():
  k, v = mod.get_population()
  print(k, v)
  
  print( mod.var )
  country = input("Pon el pais: ")
  print( mod.get_population_by_country(countries, country) )

if __name__ == '__main__':
  run()