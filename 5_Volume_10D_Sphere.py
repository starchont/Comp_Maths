import numpy as np
from numba import jit, prange


def main():

    @jit(nopython=True, parallel=True)
    def volume(dim, iterations):
        count = 0
        for _ in prange(iterations):
            point = np.random.uniform(-1.0, 1.0, int(dim))
            distance = np.linalg.norm(point)
            if distance < 1.0:
                count += 1

        return np.power(2.0, dim) * (count / iterations)

    Volume_1 = volume(10, pow(10, 6))
    print("Volume of 10D sphere: ", Volume_1)


if __name__ == "__main__":
    main()
