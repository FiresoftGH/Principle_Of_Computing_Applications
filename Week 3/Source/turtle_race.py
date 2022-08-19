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

def turtle_placement(name, color, speed, size):
    name.showturtle()
    name.shape("turtle")
    name.penup()
    name.speed(speed)
    name.color(color)
    name.turtlesize(stretch_len = size, stretch_wid = size)

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
            
def turtle_movement(name, speed, energy, state):

    if state == 0:
        while energy > 0:
            oomph = random.randint(1, speed)
            name.forward(10 * oomph)
            energy_drain = random.randint(0, 10)
            if energy_drain >= 5:
                energy -= energy_drain * 1
            if energy_drain < 5:
                    energy -= energy_drain * 0.5
    
    if state == 1:
        while energy > 0:
            oomph = random.randint(1, speed)
            name.forward(oomph)
            energy_drain = random.randint(0, 10)
            if energy_drain >= 5:
                energy -= energy_drain * 1
            if energy_drain < 5:
                    energy -= energy_drain * 0.5
    


normal_turtle = DefineTurtle("blue", 6, 1, 100, 0)
large_turtle = DefineTurtle("black", 3, 3, 150, 1)
drunk_turtle = DefineTurtle("green", 8, 1, 100, 2)
ninja_turtle = DefineTurtle("red", 10, 2, 200, 3)
giga_turtle = DefineTurtle("grey", 10, 3, 300, 4)

turtle_placement(racer_1, normal_turtle.color, normal_turtle.speed, normal_turtle.size)
turtle_placement(racer_2, large_turtle.color, large_turtle.speed, large_turtle.size)
turtle_placement(racer_3, drunk_turtle.color, drunk_turtle.speed, drunk_turtle.size)
turtle_placement(racer_4, ninja_turtle.color, ninja_turtle.speed, ninja_turtle.size)
turtle_placement(racer_5, giga_turtle.color, giga_turtle.speed, giga_turtle.size)

turtle_movement(racer_1, normal_turtle.speed, normal_turtle.energy, normal_turtle.state)
turtle_movement(racer_2, normal_turtle.speed, normal_turtle.energy, normal_turtle.state)
turtle_movement(racer_3, normal_turtle.speed, normal_turtle.energy, normal_turtle.state)
turtle_movement(racer_4, normal_turtle.speed, normal_turtle.energy, normal_turtle.state)
turtle_movement(racer_5, normal_turtle.speed, normal_turtle.energy, normal_turtle.state)


window.mainloop()
        