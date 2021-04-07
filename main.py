from pylab import *
from numpy import *
n = random.randn(100000)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(n)
axes[1].hist(n, cumulative=True, bins=50)

plt.show() 