import random as rd
import turtle
import matplotlib.pyplot as plt
import numpy as np

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
        pass
        # your code goes here 

xcor = []
ycor = []

def makeLine():
    for x in range(5):
        point = Point(rd.randint(-10, 10), rd.randint(-10, 10))
        xcor.append((point.get_x()))
        ycor.append((point.get_y()))

class Line:
    def __init__(self, list = []):
        self.list = list

    def construct(self):
        makeLine() 
        for index in range(len(xcor)):
            self.list.append([xcor[index], ycor[index]])

        xcor.clear()
        ycor.clear()
        return self.list

    def join_line(self, other):
        line_a = self.list
        line_b = other.list
        new_line = line_a + line_b
        line_b.clear()
        return new_line

    def zigzag1(self, other):
        line_3 = []
        for index in range(len(other.list)):
            if index < len(self.list):
                line_3.append(self.list[index])
            line_3.append(other.list[index])
        
        self.list.clear()
        other.list.clear()
        return line_3

    def zigzag2(self, other):
        i = 0
        for element in other.list:
            if i < len(self.list) - 1:
                self.list.insert(i + 1, element)
                i += 2
            else:
                self.list.append(element)
            
        other.list.clear()
        return self.list

object_1 = Line([])
object_2 = Line([[1, 2]])

line_1 = object_1.construct()
line_2 = object_2.construct()

print(line_1)
print(line_2)

# joined = object_1.join_line(object_2)
# print(joined)

# zigzag_1 = object_1.zigzag1(object_2)
# print(zigzag_1)

zigzag_2 = object_1.zigzag1(object_2)
print(zigzag_2)












