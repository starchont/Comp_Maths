import numpy as np
import matplotlib.pyplot as plt


def f_k(x):
    return 2/(np.pi * pow(1 - pow(x, 2), 1/2))


def g(x):
    return 1/2 * 1/(pow(1-x, 1/2))


def Inv_func(x):
    return 1 - x ** 2


N: int = 1000
accept: int = 0
value_x: list = []


while accept < N:
    num_1 = np.random.uniform(0, 1)
    y = Inv_func(num_1)
    num_2 = np.random.uniform(0, 1)
    if num_2 <= 4/np.pi * 1/(1+g(y))**(1/2):
        accept += 1
        value_x.append(y)

x_1 = np.linspace(0, 1, len(value_x))
y_2 = f_k(x_1)


# Plotting figures
plt.figure(0)
plt.hist(value_x, density=True, label="Distribution of Acceptance - Rejection algorithm")
plt.plot(x_1, y_2, label="f(x) pdf")
plt.legend()

plt.show()
