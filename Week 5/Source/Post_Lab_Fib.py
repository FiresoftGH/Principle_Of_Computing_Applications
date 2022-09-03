import sys
from time import time
import matplotlib.pyplot as plot
import numpy as np

def rfib(n):
    if n < 0:
        print("Incorrect input")
        return
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return rfib(n - 1) + rfib(n - 2)

print(rfib(100))

def ifib(n):
    if n < 0:
        print("Incorrect Input")
        return 
    else:
        result = [0, 1]
        for x in range(n):
            result.append(result[0 + x] + result[1 + x])

        print(result[n])

# ifib(9)

runtime_plot = []
n_plot = []

def plotting():
    xpoints = np.array(n_plot)
    ypoints = np.array(runtime_plot)

    plot.plot(xpoints, ypoints)
    plot.show()

# while True:
#     try:
#         n = int(input("Enter a term in fibonnaci sequence: "))
#         n_plot.append(n)
#         choice = int(input("Enter an alglorithm choice [1, 2]: "))
#         if choice not in [1, 2]:
#             print("Invalid Input")

#         elif choice == 1:
#             start = time()
#             ifib(n) 
#             end = time()
#             runtime_plot.append(end - start)
            
#         else:
#             start = time()
#             rfib(n) #print for value
#             end = time()
#             runtime_plot.append(end - start)

#         print(runtime_plot)

#         if len(runtime_plot) > 4:
#             plotting()

#     except KeyboardInterrupt:
#         sys.exit(0)

#     except ValueError:
#         print("Wrong Type")
