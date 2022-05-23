from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

#Number of trials, probability of failure
n = 5
p = (2/3)

#Binomial Random Variable
rv = binom(n, p)

#X axis
x_val = np.arange((n+1))

#PMF Values (Y axis)
pmf_val = rv.pmf(x_val)

#Plot
plt.plot(x_val, pmf_val, 'ro')
plt.vlines(x_val, 0, pmf_val, colors='k', label='Probability')
plt.legend(loc = 'best', frameon = True)

plt.show()