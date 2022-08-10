import numpy as np
from tqdm import trange


# function that selects a random number
def random_numbers():
    rng = np.random.default_rng()
    r = rng.random(1)
    return r


num: int = 100000
total: int = 0

for i in trange(0, num):
    R = random_numbers() * 60
    J = random_numbers() * 60
    if float(R) < float(J) < float(R + 15) or float(J) < float(R) < float(J + 15):
        total += 1

print("The probability of meeting is: ", total/num)
