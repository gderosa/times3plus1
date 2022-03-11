# https://www.youtube.com/watch?v=094y1Z2wpJg

import sys

x = 0
y = int(sys.argv[1])

def odd(n):
    return n % 2

def even(n):
    return not odd(n)

print("x,y")
while y != 1:
    if odd(y):
        y = y*3 + 1
    else:
        y = y // 2
    print(f"{x},{y}")
    x += 1

