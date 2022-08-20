import turtle
import random
import time
import sys

window = turtle.Screen()
window.bgcolor("white")
window.setup(width = 1200, height = 600)
window.title("Turtle Race")

racer_1 = turtle.Turtle()
racer_2 = turtle.Turtle()
racer_3 = turtle.Turtle()
racer_4 = turtle.Turtle()
racer_5 = turtle.Turtle()

racer_1.hideturtle()
racer_2.hideturtle()
racer_3.hideturtle()
racer_4.hideturtle()
racer_5.hideturtle()

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

class DefineTurtle:
    def __init__(self, color, speed, size, energy, state):
        self.state = state
        self.size = size
        self.color = color
        self.speed = speed
        self.energy = energy

    def turtle_placement(self):
        if self.color == "black":
            racer_1.setpos(-500, 100)
        if self.color == "blue":
            racer_1.setpos(-500, 0)
        if self.color == "green":
            racer_1.setpos(-500, -100)
        if self.color == "red":
            racer_1.setpos(-500, 200)
        if self.color == "grey":
            racer_1.setpos(-500, -200)

    def turtle_movement(self):
        if self.state == 0:
            racer_1.forward(100)
        if self.state == 1:
            racer_2.forward(120)
        if self.state == 2:
            racer_3.forward(140)
        if self.state == 3:
            racer_4.forward(160)
        if self.state == 4:
            racer_5.forward(160)