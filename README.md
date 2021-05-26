# Drawing square function chart


# Instalation

1. Clone this repository
2. Activate your venv
3. Move into this repository
4. Install dependencies - `pip3 install -r requirements.txt`
5. Run the code - `python3 main.py`

### How to use
Run `python3 main.py`, if you completed instalation. Program is bassicaly self explanatory - you need to input your quadratic function general form (a, b and c), as well as range you want to look at. You can also go with default values, which will work as well.

### Docs

Libraries used can be viewed at requirements.txt file.

```
def squareFunction(x, a, b, c):
    return a*x**2 + b*x + c
```

This function is simply [quadratic function](https://www.google.com/search?q=quadratic+function+general+form&oq=qua&aqs=chrome.0.69i59j69i57j0i433j0l2j69i65j69i61l2.762j0j7&sourceid=chrome&ie=UTF-8 "quadratic function").

It gives result, based on X and given parameters a, b, c (which describes this function)



Another method in this code is drawChart() - it shows a window, cointaining a chart based on given information.
```
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
```




#### Pseudocode:

1. Initializing GUI, containing form.
2. When user clicks "Submit" button code moves forward (with values given in the form)
3. When user clicks "Cancel" button program stops.
4. Linspace of 100 values in given range is created.
5. This function is run over all those 100 values
6. Chart of given values is drawn
