# https://www.youtube.com/watch?v=094y1Z2wpJg


import sys

import matplotlib.pyplot as plt


plt.rcParams['font.family']     = 'monospace'
plt.rcParams['font.size']       = 6.0
plt.rcParams['lines.linewidth'] = 1


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

def plot(Y):
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)
    ax.set_title(f'"3y+1" problem')
    ax.set_yscale('log')
    ax.plot(
        range(len(Y)), Y,
        label=f'y_0 = {Y[0]}'
    )
    ax.set_xlabel('n')
    ax.set_ylabel('y_n')
    ax.legend()
    plt.show()

    # Optional: If you have an ATI Radeon: https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-21-10

def main():
    y_0 = int(float(sys.argv[1]))
    Y = sequence(y_0)
    plot(Y)


main()

