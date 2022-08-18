import turtle

import time
from winreg import DisableReflectionKey

window = turtle.Screen()
window.bgcolor("white")
window.setup(width = 1200, height = 600)
window.title("Turtle Race")
turtle.hideturtle()

def draw_background():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.pensize(3)
    pen.color("red")
    pen.goto(550, 500)
    pen.pendown()
    pen.right(90)
    pen.forward(1000)

draw_background()

class NormalTurtle:
    def __init__(self, name, color, speed, size, energy, state):
        self.name = name
        name = turtle.Turtle()
        name.shape("turtle")
        name.penup()

        self.color = name.color(color)
        self.speed = name.speed(speed)
        self.size = name.turtlesize(stretch_len = size, stretch_wid = size)
        self.energy = energy
        self.state = state

        if color == "black":
            name.setpos(-500, 100)
        if color == "blue":
            name.setpos(-500, -100)
        if color == "green":
            name.setpos(-500, 0)
        if color == "red":
            name.setpos(-500, -200)
        if color == "grey":
            name.setpos(-500, 200)
    
    # def movement_calculations(self):

# class TurtleMovement:
#     def __init__(self, name, state, energy):
#         self.state = state
#         self.energy = energy
#         if state == 0:
#             while energy > 0:
#                 name.foward(200)
                
                


normal_turtle = NormalTurtle("normal", "blue", 6, 1, 100, 0)
large_turtle = NormalTurtle("large", "black", 3, 3, 150, 0)
drunk_turtle = NormalTurtle("drunk", "green", 8, 1, 100, 1)
ninja_turtle = NormalTurtle("ninja", "red", 10, 2, 200, 2)
giga_chad_turtle = NormalTurtle("giga_chad","grey", 10, 3, 300, 3)

window.mainloop()
        