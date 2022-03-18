# https://www.youtube.com/watch?v=094y1Z2wpJg


from os.path import exists
import json

import matplotlib.pyplot as plt


CACHEFILE = '.cache.json'


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

def set_plotting(plt):
    plt.rcParams['font.family']     = 'monospace'
    plt.rcParams['font.size']       = 14.0
    plt.rcParams['lines.linewidth'] = 1.5
    # "Full HD" 1920x1080
    plt.rcParams['figure.figsize']  = [19.2, 10.8]
    plt.rcParams['savefig.dpi']     = 100

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

    figfiles        = [
        'plots/svg/%012d.svg' % y_init_max,
        'plots/png/%012d.png' % y_init_max,
        'plots/jpg/%012d.jpg' % y_init_max
    ]

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
    for filename in figfiles:
        if exists(filename):
            print('Found:   %s' % filename)
        else:
            print('Writing: %s' % filename)
            plt.savefig(filename)
    plt.close()
    print()

def main():
    cache   = [ ]

    tallest = [0]
    widest  = [0]
    y_0 = 1
    x_MAX   = 0
    y_MAX   = 0

    set_plotting(plt)

    if exists(CACHEFILE):
        with open(CACHEFILE) as f:
            cache = json.load(f)
        print('Loading initial data from cache:', end='\n\n')
        for cache_item in cache:
            tallest_0   = cache_item['tallest_0']
            widest_0    = cache_item[ 'widest_0']
            tallest     = sequence(   tallest_0)
            widest      = sequence(    widest_0)
            plot(tallest, widest)
        y_0 = max(tallest_0, widest_0)

    print('Computing:', end='\n\n')
    while True:
        if not y_0 % 1e5:
            print(' %.1f M' % (y_0/1e6), end='\r')
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
            cache.append({
                'tallest_0' : tallest[  0],
                'widest_0'  : widest[   0]
            })
            with open(CACHEFILE, 'w') as f:
                json.dump(cache, f, indent=2)
        y_0 += 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

