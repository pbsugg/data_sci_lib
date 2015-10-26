from matplotlib import pyplot as chart

# testing out functionality of matplotlib


test = [1, 1, 2, 3, 5 ,8, 13, 21, 34, 55]
iterations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# create plot
chart.plot(iterations, test, linestyle = 'solid')

# title

chart.title("Fibonacci")
chart.show()
