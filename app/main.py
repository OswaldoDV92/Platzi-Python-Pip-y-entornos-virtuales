"""from unicodedata import name
from unittest import result"""
import mi_modulo

data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population': 300
    }
]

def run():
    keys, values = mi_modulo.get_population()
    print(keys, values)

    print(mi_modulo.A)

    country = input('Escribe un país: ')
    result = mi_modulo.population_by_country(data, country.title())
    print(result)

if __name__ == '__main__':
    run()