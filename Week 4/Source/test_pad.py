import numpy as np
import matplotlib.pyplot as plot

test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

xpoints = np.array(test_array)
ypoints = np.array(test_array)

plot.plot(xpoints, ypoints)
plot.show()