import matplotlib.pyplot as plt
import numpy as np

ypoints = np.loadtxt('Automation\Pyplot\example.txt', delimiter=',', usecols=1)  
xpoints = np.loadtxt('Automation\Pyplot\example.txt', delimiter=',', usecols=0)   
print(np.average(ypoints)
)
# plt.plot(xpoints, ypoints)
# plt.show()