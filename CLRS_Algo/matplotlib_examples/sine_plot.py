import matplotlib.pyplot as plt
import numpy as np

# example of matplotlib from some random website

t = np.arange(0.0, 2.0, 0.01) # get x-axis values
s = 1 + np.sin(2*np.pi*t) # get y-axis values
plt.plot(t, s) # command plot(x,y)

#plot decorations
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('Simple Plot')
plt.grid(True)
plt.savefig("test.png")
plt.show()