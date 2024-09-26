#%%
from xcorr import xcorr
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.grid'] = True

# load positive cases data
positives_file = 'data/Test_pos_over_time.csv'
positives_data = np.genfromtxt(positives_file, delimiter=';', dtype=str)
i_start = np.where(positives_data[:, 0] == '01/10/2020')[0][0]
i_end = np.where(positives_data[:, 0] == '28/02/2021')[0][0]
positives_data = positives_data[i_start:i_end, 1].astype(int)

# load hospitalize cases data
hospitalized_file = 'data/Newly_admitted_over_time.csv'
hospitalized_data = np.genfromtxt(hospitalized_file, delimiter=';', dtype=str)
i_start = np.where(hospitalized_data[:, 0] == '2020-10-01')[0][0]
i_end = np.where(hospitalized_data[:, 0] == '2021-02-28')[0][0]
hospitalized_data = hospitalized_data[i_start:i_end, -1].astype(int)
#%%
k = int(positives_data.shape[0]/2)

r = xcorr(positives_data, hospitalized_data, k)
uk = np.arange(-k,k+1)
plt.plot(uk, r, color = 'b', label='N=30 a=0.1')

# %%
