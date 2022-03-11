# https://www.youtube.com/watch?v=094y1Z2wpJg

import sys

import matplotlib.pyplot as plt

x = 0
y = int(sys.argv[1])

X = []
Y = []

def odd(n):
    return n % 2

while y != 1:
    if odd(y):
        y = y*3 + 1
    else:
        y = y // 2

    x += 1

    # print(y)  # DEBUG

    X.append(x)
    Y.append(y)

plt.plot(X, Y)
plt.show()

