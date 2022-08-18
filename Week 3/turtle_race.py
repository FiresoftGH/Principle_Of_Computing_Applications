import turtle

window = turtle.Screen()
window.bgcolor("white")


class turtle_class:
    def __init__(self, name, speed, energy, alcohol):
        racer = turtle.Turtle()
        self.name = racer.color("green")
        self.speed = racer.speed
        self.energy = energy
        self.alcohol = alcohol

drunk_turtle = turtle_class("Drunk_Turtle", "Speed")
        