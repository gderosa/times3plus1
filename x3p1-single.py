# https://www.youtube.com/watch?v=094y1Z2wpJg


import sys

import matplotlib.pyplot as plt

from x3p1 import set_plotting, sequence


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
    set_plotting(plt)

    y_0 = int(float(sys.argv[1]))
    Y = sequence(y_0)
    plot(Y)


main()

