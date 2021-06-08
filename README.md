### Jak
Uruchom `python3 main.py`, jeśli zakończyłeś instalację. Program jest w zasadzie oczywisty - musisz wprowadzić ogólną formę funkcji kwadratowej (a, b i c), a także zakres, na który chcesz się przyjrzeć. Możesz także wybrać wartości domyślne, które również będą działać.

### Dokumenty

Użyte biblioteki można przeglądać w pliku Requirements.txt.

````
def FunkcjaKwadratowa(x, a, b, c):
     zwróć a*x**2 + b*x + c
````

Ta funkcja to po prostu [funkcja kwadratowa](https://www.google.com/search?q=quadratic+function+general+form&oq=qua&aqs=chrome.0.69i59j69i57j0i433j0l2j69i65j69i61l2.762j0j7&sourceid=chrome&ie=UTF-8 „funkcja kwadratowa”) .

Daje wynik na podstawie X i podanych parametrów a, b, c (co opisuje tę funkcję)
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
`
