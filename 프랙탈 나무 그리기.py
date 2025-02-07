import math
from matplotlib import pyplot as plt

colors = ["#984b00", "#317c00"]


def fixed_tree(x, y, angle, length, order, total):
    if order > 0:
        x2 = x + (math.cos(math.radians(angle)) * length)
        y2 = y + (math.sin(math.radians(angle)) * length)
        color = colors[0 if order >= 3 else 1]
        plt.plot([x, x2], [y, y2], color)

        fixed_tree(x2, y2, angle - 30, length * 0.8, order - 1, total)
        fixed_tree(x2, y2, angle + 30, length * 0.8, order - 1, total)


if __name__ == '__main__':
    order = 12
    fixed_tree(x=100, y=100,
               angle=90,
               length=70,
               order=order,
               total=order)

    plt.show()