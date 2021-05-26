import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg

def squareFunction(x, a, b, c):
    return a*x**2 + b*x + c

def drawChart(a, b, c, first, last):

    # converting values to floats
    a = float(a)
    b = float(b)
    c = float(c)
    first = float(first)
    last = float(last)

    # 100 linearly spaced numbers
    x = np.linspace(last, first, 100)

    # the function
    y = squareFunction(x, a, b, c)

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x,y, 'r')

    # show the plot
    plt.show()

sg.theme('SandyBeach')
layout = [
    [sg.Text('Enter parameters (general form) of your square function:')],
    [sg.Text('a', size =(15, 1)), sg.InputText(default_text="3")],
    [sg.Text('b', size =(15, 1)), sg.InputText(default_text="4")],
    [sg.Text('c', size =(15, 1)), sg.InputText(default_text="5")],
    [sg.Text('Define range of your function:')],
    [sg.Text('first', size =(15, 1)), sg.InputText(default_text="10")],
    [sg.Text('last', size =(15, 1)), sg.InputText(default_text="-10")],
    [sg.Submit(), sg.Cancel()]
]

# getting values
window = sg.Window('Math function GUI', layout)
event, values = window.read()

# drawing chart
drawChart(values[0], values[1], values[2], values[3], values[4])
