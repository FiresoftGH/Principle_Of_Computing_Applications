import sys
from this import d
import matplotlib.pyplot as plot
import random
import math

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

point_objects = []
distance_objects = []

while True:
    try:
        number_of_points = int(input("How many times do you want the loop to run?: "))
        max_value = int(input("Max Value of coordinates: "))
        for index in range(number_of_points):
            point_objects.append(Point(random.randint(-max_value, max_value), random.randint(-max_value, max_value)).get_coord())
            internal_index = len(point_objects[index])
            # point_count = len(point_objects)

            if index != 0:
                distance_objects.append(Point(point_objects[index][internal_index - 1], point_objects[index][internal_index]).distance(
                    Point(point_objects[index - 1][internal_index - 1], point_objects[index - 1][internal_index])))
        
        print(point_objects)
        for x in range(10):
            print("")

        distance_objects.append(Point(point_objects[index][internal_index - 1], point_objects[index][internal_index]).distance(
                    Point(point_objects[index - 1][internal_index - 1], point_objects[index - 1][internal_index])))
        print(distance_objects)

        distance_objects = []
        point_objects = []
        
    except KeyboardInterrupt:
        sys.exit(0)