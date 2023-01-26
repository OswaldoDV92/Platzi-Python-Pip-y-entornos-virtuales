import read_csv, charts

if __name__ == '__main__':
    data = read_csv.read_csv('./data.csv')
    percentage = list(map(lambda row: row['World Population Percentage'], data))
    country_name = list(map(lambda row: row['Country/Territory'], data))
    charts.generate_pie_chart('World', country_name, percentage)
