from bokeh.plotting import figure, output_file, show

def run():
    output_file('simple_graphic.html')
    fig = figure()

    total_values = int(input('Cuantos valores quires graficar: '))
    x_values = list(range(total_values))
    y_values = []

    for x in x_values:
        val = int(input(f'Valor y para {x}: '))
        y_values.append(val)

    fig.line(x_values, y_values, line_width=2)
    show(fig)


if __name__ == '__main__':
    run()
