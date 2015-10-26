# build a few charts to illustrate expansion of complexity formulas, big O
# O(n), O(n**2), O(2**n), O(log n)

# define the formula
# for some X interval...plot every Y value

from matplotlib import pyplot as data
import math

x = range(50)
y = []
for i in x:
    y.append(x[i]**2)

data.plot(x, y, linestyle = 'dotted')
data.xlabel("Number of iterations")
data.ylabel("n^2")

data.show()

x = range(1,500)
y = []
for j in x:
    y.append(math.log(j, 2))

data.plot(x, y, linestyle = 'solid')
data.xlabel("Number of iterations")
data.ylabel("n^2")

data.show()
