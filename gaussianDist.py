import numpy as np
import matplotlib.pyplot as plt

frameid=100
mean=frameid/2
std=frameid/3
weights=np.exp(-0.5*((np.arange(frameid)-mean)/std)**2)
weights/=weights.sum()
indexes=list(range(frameid))
plt.figure(figsize=(10,6))
plt.plot(indexes,weights,label="line")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()