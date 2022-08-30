import sys
import random
import math
import matplotlib.pyplot as plot
import numpy as np
from time import time
import keyboard as kb

distance_compare = []
runtime_compare = []

class Point: 
    def __init__(self, x_init, y_init): 
        self.x = x_init 
        self.y = y_init 
    def get_x(self): 
        return self.x 
    def get_y(self): 
        return self.y 
    def __repr__(self): 
        return "".join(["(", str(self.x), ",", str(self.y), ")"]) 
    def __str__(self): 
        return "(%s,%s)" % (self.x, self.y) 
    def get_coord(self):
        coords = [self.x, self.y]
        return coords
    def distance(self, other):
        distance = math.sqrt((abs(self.x - other.x))**2 +(abs(self.y - other.y)**2))
        distance = round(distance, 2)
        data = [distance, (self.x, self.y), (other.x, other.y)]
        return data
    def findClosest(distance_objects):
        start = time()
        for index in range(len(distance_objects)):
            distance_compare.append(distance_objects[index][0])

        minimum = min(distance_compare)
        minimum_index = distance_compare.index(minimum)
        # print(min(distance_compare))
        print("The answer is: ", distance_objects[minimum_index])
        end = time()
        runtime = end - start
        runtime_compare.append(runtime)
        print(runtime_compare)

point_count = []
distance_objects = []

def plot_runtime():
    xpoints = np.array(point_count)
    ypoints = np.array(runtime_compare)

    plot.plot(xpoints, ypoints)
    plot.show()

while True:
    try:
        number_of_points = int(input("How many times do you want the loop to run? (Two times the number of points): "))
        max_value = int(input("Max Value of coordinates: "))
        for index in range(number_of_points):
            distance_objects.append(Point(random.randint(-max_value, max_value), 
            random.randint(-max_value, max_value)).distance(Point(random.randint(-max_value, max_value), 
            random.randint(-max_value, max_value))))
            # point_objects.append(Point(random.randint(-max_value, max_value), random.randint(-max_value, max_value)).get_coord())

        point_count.append(number_of_points / 2)
        # print(distance_objects)
        Point.findClosest(distance_objects)
        distance_objects = []
        distance_compare = []

        if len(runtime_compare) >= 5:
            plot_runtime()
        
    except KeyboardInterrupt:
        sys.exit(0)

    except TypeError:
        sys.exit(0)