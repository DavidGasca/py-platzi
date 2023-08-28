import matplotlib.pyplot as plt
import csv

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()
  
def read_csv(path, country):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next( reader )
    for row in reader:
      if row[2] == country:
        iterable = zip(header, row)
        cntry_dict = {key: value for key, value in iterable}
        return cntry_dict
    return False

def get_population_by_year(country):
  years = ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']
  population = [int(country.get('2022 Population')), int(country.get('2020 Population')),
               int(country.get('2015 Population')), int(country.get('2010 Population')),
               int(country.get('2000 Population')), int(country.get('1990 Population')),
               int(country.get('1980 Population')), int(country.get('1970 Population'))]
  return years, population


data = read_csv('./world_population.csv', 'Mexico')
if data != False:
  years, population = get_population_by_year(data)
  print(years)
  print(population)
  generate_bar_chart(years, population)
else:
  print('Pais on encontrado')

