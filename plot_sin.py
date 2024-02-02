# %%
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.ndimage import gaussian_filter1d 

f = 1 
t = np.linspace(0, 3, 1000) 
x = np.sin(2 * np.pi * f * t)
x += np.random.normal(0,1,size=(len(x))) * 0.1 
x_smoothed = gaussian_filter1d(x, sigma=20) 

plt.plot(t, x, label=f'{f}[Hz]')  
plt.plot(t, x_smoothed, label='smoothed') 
plt.legend() 
plt.show() 

# %%
