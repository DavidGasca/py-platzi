import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  
  '''
  data = list(filter(lambda item : item['Continent'] == 'North America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values, country['Country/Territory'])
  
  
if __name__ == '__main__':
  run()

''' REFERENCIAS
https://www.w3schools.com/python/matplotlib_pyplot.asp
https://matplotlib.org/stable/plot_types/index.html
https://www.kaggle.com/datasets/d893bc6eb4370c2fd7b87bcf41972963b607202a1683f576700c52e6ecd4ab2a/code?resource=download
https://www.kaggle.com/code/mohidabdulrehman/eda-world-population-plotly
https://www.kaggle.com/code/nguyenthicamlai/eda-on-world-population
https://www.w3schools.com/python/python_file_open.asp
https://realpython.com/working-with-files-in-python/
https://www.qlik.com/es-es/products/qlik-sense

'''