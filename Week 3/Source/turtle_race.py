import turtle

import time

window = turtle.Screen()
window.bgcolor("white")
window.setup(width = 1200, height = 600)
window.title("Turtle Race")
turtle.hideturtle()

def draw_background():
    pen = turtle.Turtle()
    pen.penup()
    

class turtle_class:
    def __init__(self, color, speed, size, energy, state):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.penup()

        self.color = racer.color(color)
        self.speed = racer.speed(speed)
        self.size = racer.turtlesize(stretch_len = size, stretch_wid = size)
        self.energy = energy
        self.state = state

        if color == "black":
            racer.setpos(-500, 100)
        if color == "blue":
            racer.setpos(-500, -100)
        if color == "green":
            racer.setpos(-500, 0)

        

normal_turtle = turtle_class("blue", 6, 1, 100, 0)
large_turtle = turtle_class("black", 3, 3, 150, 0)
drunk_turtle = turtle_class("green", 8, 1, 100, 1)
ninja_turtle = turtle_class("red", 10, 2, 200, 2)


window.mainloop()
        