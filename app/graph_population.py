import csv, charts
#import matplotlib.pyplot as plt

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        header = next(reader)
        data = []
        
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        
        return data

def find_country(country):
    data = read_csv('./data.csv')
    country = list(filter(lambda item: item['Country/Territory'] == country, data))
    return country

def get_population(country):
    population = {
        '1970': 0,
        '1980': 0,
        '1990': 0,
        '2000': 0,
        '2010': 0,
        '2015': 0,
        '2020': 0,
        '2022': 0,
    }
    
    values = [ int(country[element + ' Population']) for element in population]
    year = [ element for element in population]
    return year, values

if __name__ == '__main__':
    country = input('Ingresa un país: ')
    result = find_country(country.title())
    country = result[0] # recupera el diccionario de la lista
    #print(country['Country/Territory'])
    year, values = get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], year, values)