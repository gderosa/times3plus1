# https://www.youtube.com/watch?v=094y1Z2wpJg


import sys
from os.path import exists
from time import sleep
import json

import matplotlib.pyplot as plt


CACHEFILE                       = '.cache.progr.json'

plt.rcParams['font.family']     = 'monospace'
plt.rcParams['font.size']       = 6.0
plt.rcParams['lines.linewidth'] = 2/3


def odd(n):
    return n % 2

def next(y):
    if odd(y):
        return y*3 + 1
    else:
        return y // 2

def sequence(y_0):
    y = y_0
    Y = [y]
    while y > 1:
        y = next(y)
        Y.append(y)
    return Y

def plot(tallest, widest):
    max_x           = len(widest)
    max_y_widest    = max(widest)
    max_x_tallest   = len(tallest)
    max_y           = max(tallest)

    tallest_X   = range(max_x_tallest)
    tallest_Y   = tallest
    widest_X    = range(max_x)
    widest_Y    = widest

    tallest_y_init  = tallest[0]
    widest_y_init   = widest[0]

    y_init_max      = max(tallest_y_init, widest_y_init)
    filename        = 'plots/%012d.svg' % y_init_max

    yscale = 'log'

    fig, ax = plt.subplots()
    fig.set_tight_layout(True)
    ax.set_title(f'"3y+1" problem')
    ax.set_yscale(yscale)
    ax.plot(
        tallest_X, tallest_Y,
        label=f'"Tallest":\ny_0    = {tallest_y_init}\ny_max  = {max_y       }\nx_max  = {max_x_tallest}'
    )
    ax.plot(
        widest_X,  widest_Y,
        label=f'"Widest": \ny_0    = { widest_y_init}\ny_max  = {max_y_widest}\nx_max  = {max_x        }'
    )
    ax.set_xlabel('n')
    ax.set_ylabel('y_n')
    ax.legend()
    print('Writing: %s' % filename)
    plt.savefig(filename)
    plt.close()

    # Optional: If you have an ATI Radeon: https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-21-10

def save_data(x_MAX, y_MAX, y_0):
    data = {
        'x_MAX': x_MAX,
        'y_MAX': y_MAX,
        'y_0': y_0
    }
    with open(CACHEFILE, 'w') as f:
        json.dump(data, f)

def main():
    tallest = [0]
    widest  = [0]
    if len(sys.argv) > 1:
        y_0 = int(float(sys.argv[1]))
    else:
        y_0 = 1
    x_MAX   = 0
    y_MAX   = 0

    if exists(CACHEFILE):
        with open(CACHEFILE) as f:
            cache = json.load(f)
        x_MAX   =           cache['x_MAX'   ]
        y_MAX   =           cache['y_MAX'   ]
        y_0     = max(y_0,  cache['y_0'     ])

    while True:
        found = False
        Y = sequence(y_0)
        y_max = max(Y)
        x_max = len(Y)
        if y_max > y_MAX:
            y_MAX = y_max
            tallest = Y
            found = True
        if x_max > x_MAX:
            x_MAX = x_max
            widest = Y
            found = True
        if found:
            plot(tallest, widest)
            save_data(x_MAX, y_MAX, y_0)
        y_0 += 1


try:
    main()
except KeyboardInterrupt:
    pass

