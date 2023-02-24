import read_csv, charts
import pandas as pd

if __name__ == '__main__':
    #data = read_csv.read_csv('./data.csv')
    #percentage = list(map(lambda row: row['World Population Percentage'], data))
    #country_name = list(map(lambda row: row['Country/Territory'], data))
    
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'South America']
    country_name = df['Country/Territory'].values
    percentage = df['World Population Percentage'].values

    charts.generate_pie_chart('World', country_name, percentage)
