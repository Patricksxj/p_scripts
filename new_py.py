
import numpy as np
x = np.random.uniform(1, 100, 1000)
y = np.log(x) + np.random.normal(0, .3, 1000)

from matplotlib import pyplot


pyplot.plot(x,np.log(x),'r')


pyplot.scatter(x,y,c='b',s=1)

pyplot.scatter(x,np.log(x),c='r',s=3)

pyplot.show()