from time import time
from matplotlib import pyplot as plt
import numpy as np

runtime = []

# Single For loop
def counter1(n):
    start = time()
    result = 0
    for x in range(n):
        result += 1
    end = time()
    operator = end - start
    runtime.append(operator)
    return result

# Nested For loop
def counter2(n):
    start = time()
    result = 0
    for x in range(n):
        result += 1
        for y in range(n // 2):
            result -= 1
    end = time()
    operator = end - start
    runtime.append(operator)
    return result

# Non-nested loop
def counter3(n):
    start = time()
    result = 0
    for x in range(n):
        result += 1
    for y in range(n // 2):
        result -= 1
    end = time()
    operator = end - start
    runtime.append(operator)
    return result

# Creating input list and graphing

inputs = []
inputs = [500 ,1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

def makeInput(size):
    number = 0
    for x in range(size):
        number += 20
        inputs.append(number)

makeInput(500)

def makeGraph(xcor = [], ycor = []):
    # xcor.sort()
    # ycor.sort()
    xplot = np.array(xcor)
    yplot = np.array(ycor)
    
    plt.plot(xplot, yplot)
    plt.show()

# Testing the runtime

def testCase():
    for elements in inputs:
        counter3(elements)

testCase()
makeGraph(inputs, runtime)



