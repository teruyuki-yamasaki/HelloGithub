# %%
import numpy as np 
import matplotlib.pyplot as plt 

f = 1 
t = np.linspace(0, 3, 1000) 
x = np.sin(2 * np.pi * f * t)
x += np.random.normal(0,1,size=(len(x))) * 0.1 

plt.plot(t, x, label=f'{f}[Hz]')  
plt.show() 

# %%
