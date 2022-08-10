import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange


# Definition of functions
def init_lattice(n):
    lattice = np.random.choice([1, -1], size=(n, 1))
    return lattice


def prob(delta_e, k, temp):
    return np.exp(-delta_e/(k*temp))


# Initialization of constants and arrays
N: int = pow(10, 4)
energy_new: float = 0.0
energy_old: float = 0.0
spin = init_lattice(N)
T_1: np.ndarray = np.array([1, 10, 20])
iterations: int = 100000
mean_mag: np.ndarray = np.zeros(iterations)
time: np.ndarray = np.linspace(1, iterations+1, iterations)


# Starting monte carlo simulation
for value in T_1:
    for iter_1 in trange(iterations):
        num_1 = np.random.randint(low=1, high=N-1)
        initial_spin = spin[num_1]
        final_spin = -spin[num_1]
        old_energy = - initial_spin * spin[num_1 - 1] - initial_spin * spin[num_1 + 1]
        energy_new = -final_spin * spin[num_1 - 1] - final_spin * spin[num_1 + 1]
        delta_E = energy_new - energy_old
        rng = np.random.default_rng()
        num_2 = rng.random()
        if num_2 < prob(delta_E, 1, value):
            spin[num_1] = final_spin
        else:
            spin[num_1] = initial_spin
        mean_mag[iter_1] = np.sum(spin)
    plt.figure(0)
    plt.plot(np.log(time), mean_mag/iterations, label="T = " + str(value))

# Plotting figures
plt.figure(0)
plt.title("Mean value of Magnetization vs Time")
plt.xlabel("Time")
plt.ylabel("<M>")
plt.grid()
plt.legend()
plt.show()
