import matplotlib.pyplot as plt # plt es el alias de matplotlib.pyplot

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.savefig(f'chart_{name}_final.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 80]
    name = 'pie'
    #generate_bar_chart(labels, values)
    generate_pie_chart(name, labels, values)