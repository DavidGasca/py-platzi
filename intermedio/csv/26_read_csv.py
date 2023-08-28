import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next( reader )
    data = []
    for row in reader:
      iterable = zip(header, row)
      print( list(iterable) )
      cntry_dict = {key: value for key, value in iterable}
      data.append(cntry_dict)
    return data

data = read_csv('./world_population.csv')
print( data )