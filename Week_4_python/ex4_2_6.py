#%%
import numpy as np
from random import seed
import matplotlib.pyplot as plt
seed(42)

# generate signal
nsamp = 200
H = np.array([1, 0.8, 0.2])
u = np.random.normal(size = nsamp)

# LMS parms
mu = 0.1
delta = 1e-6

# reserve mem
w = np.zeros((len(H), nsamp+1))
e = np.zeros(nsamp)

# LMS loop
w_n = np.zeros((len(H)))
for it in range(len(H), nsamp+1):
    u_n = np.flip(u[it-len(H):it]).T
    d = H.T @ u_n
    e_n = 0 # complete the line
    w_n = 0 # complete the line

    # store values for later plotting
    e[it-1] = e_n
    w[:, it] = w_n

# plot results
# complete code here
