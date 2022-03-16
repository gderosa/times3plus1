# https://www.youtube.com/watch?v=094y1Z2wpJg

# import json

from fileinput import filename
import matplotlib.pyplot as plt


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
    filename        = 'plots/%012d.png' % y_init_max

    if max_y_widest / max_y > 0.1:
        yscale = 'linear'
    else:
        yscale = 'log'

    plt.rcParams['font.family'] = 'monospace'
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)
    ax.set_title(f'"3y+1" problem')
    ax.set_yscale(yscale)
    ax.plot(
        tallest_X, tallest_Y, linewidth=0.85,
        label=f'"Tallest":\ny_0    = {tallest_y_init}\ny_max  = {max_y       }\nx_max  = {max_x_tallest}'
    )
    ax.plot(
        widest_X,  widest_Y, linewidth=0.85,
        label=f'"Widest": \ny_0    = { widest_y_init}\ny_max  = {max_y_widest}\nx_max  = {max_x        }'
    )
    ax.set_xlabel('n')
    ax.set_ylabel('y_n')
    ax.legend()
    print('Writing: %s' % filename)
    plt.savefig(filename, dpi=600)
    plt.close()

    # Optional: If you have an ATI Radeon: https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-21-10

def main():
    tallest = [0]
    widest  = [0]
    y_0     = 1
    x_MAX   = 0
    y_MAX   = 0
    while True:
        print(y_0, end='\r')
        Y = sequence(y_0)
        y_max = max(Y)
        x_max = len(Y)
        if y_max > y_MAX:
            y_MAX   = y_max
            tallest = Y
            plot(tallest, widest)
        if x_max > x_MAX:
            x_MAX   = x_max
            widest = Y
            plot(tallest, widest)
        y_0 += 1


main()

