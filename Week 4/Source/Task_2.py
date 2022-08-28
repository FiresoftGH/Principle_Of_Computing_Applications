import sys
import matplotlib.pyplot as plot
import random
import math
import keyboard as kb

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
    def distance(self, other):
        distance = math.sqrt((abs(self.x - other.x))**2 +(abs(self.x - other.x)**2))
        return distance

point_objects = []

while len(point_objects) <= 0:
    try:
        number_of_points = int(input("Enter number of points: "))
        max_value = int(input("Max Value: "))
        for index in range(number_of_points):
            point_objects.append(Point(random.randint(-max_value, max_value), 
            random.randint(-max_value, max_value)))
            
        
        # print(point_objects)
        print(point_objects[0])
        
    except KeyboardInterrupt:
        sys.exit(0)