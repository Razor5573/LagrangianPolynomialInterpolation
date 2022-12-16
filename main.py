import math
import numpy as np

from matplotlib import pyplot as plt


def l(x, num, nodes):
    basis_pol = 1
    step = (2 / (nodes - 1))
    x_i = -1 + step * (num)
    j = 0
    for i in np.arange(-1, 1, step):
        if j != num:
            basis_pol *= (x - i) / (x_i - i)
        j += 1
    return basis_pol


def interpolation_polynomial_value(x, nodes):
    L = 0.0
    step = (2 / (nodes - 1))
    j = 0
    for i in np.arange(-1, 1, step):
        x_i = -1 + step * j
        val = f(x_i)
        L += val * l(x, j, nodes)
        j += 1
    return L


def f(arg):
    return math.pow(arg, 2) + 1 - math.acos(arg)


nodes_count = int(input())
point = float(input())

L = interpolation_polynomial_value(point, nodes_count)
print('Margin of error: ', math.fabs(L - f(point)))


x = np.arange(-1, 1, 0.00001)
f2 = np.vectorize(f)

x_pol = np.arange(-1, 1, (2 / (nodes_count - 1)))
f_pol = np.vectorize(interpolation_polynomial_value)

x_pol_1 = np.arange(-1, 1, (2 / ((2 * nodes_count) - 1)))

plt.plot(x, f2(x), 'r', 'Source function')
plt.plot(x_pol, f_pol(x_pol, nodes_count), 'b', 'Polynomial function')
plt.plot(x_pol_1, f_pol(x_pol_1, 2 * nodes_count), 'g', 'x2 Polynomial function')

plt.show()
