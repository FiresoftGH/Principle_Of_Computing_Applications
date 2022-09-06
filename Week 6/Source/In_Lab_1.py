import random as rd
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

class Line:
    def __init__(self, x_init, y_init):
        super().__init__(x_init, y_init)

    def construct(self, list):
        list.append((self.x, self.y))
        print(list)

objects = []

for x in range(5):
    objects.append(Point(rd.randint(-10, 10), rd.randint(-10, 10)))
    
print(objects)

line_objects = []

for stuff in objects:
    print(stuff)



