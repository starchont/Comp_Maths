import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pylab as py


def exp_gen(lam):
    rng = np.random.default_rng()
    x = rng.random()
    # Reverse of pdf
    y = - np.log(1 - x) / lam
    return y


num = 10000
data = np.zeros(num)  # 1000000*[0]
for i in range(num):
    q = exp_gen(1)
    data[i] = q

# Making histogram
num_bins = 20
n, bins, patches = plt.hist(data, num_bins, facecolor='blue', alpha=0.5)
plt.xlabel('q')
plt.ylabel('Probability')
plt.show()

# Making qq plot
stats.probplot(data, dist="expon", plot=py)
py.show()
