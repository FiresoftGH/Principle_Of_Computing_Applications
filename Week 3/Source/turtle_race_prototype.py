import turtle
import random
import threading
import queue

window = turtle.Screen()
window.bgcolor("white")
window.setup(width = 1200, height = 600)
window.title("Turtle Race")

racer_1 = turtle.Turtle()
racer_2 = turtle.Turtle()
racer_3 = turtle.Turtle()
racer_4 = turtle.Turtle()
racer_5 = turtle.Turtle()
text_pen = turtle.Turtle()

racer_1.shape("turtle")
racer_2.shape("turtle")
racer_3.shape("turtle")
racer_4.shape("turtle")
racer_5.shape("turtle")

racer_1.hideturtle()
racer_2.hideturtle()
racer_3.hideturtle()
racer_4.hideturtle()
racer_5.hideturtle()
text_pen.hideturtle()

def victory_message(color):
    text_pen.penup()
    text_pen.goto(0, 100)
    text_pen.write(color, True, align = "center", font = ("Arial", 14, "normal"))
    text_pen.goto(50, 100)
    text_pen.write("wins", True, align = "center", font = ("Arial", 14, "normal"))

# victory_message("green")

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

    def placement(self):
        if self.color == "black":
            racer_1.penup()
            racer_1.showturtle()
            racer_1.setpos(-500, 100)
            racer_1.color(self.color)
            racer_1.speed(self.speed)
            racer_1.shapesize(stretch_len = self.size, stretch_wid = self.size)
            racer_2.showturtle()

        if self.color == "blue":
            racer_2.penup()
            racer_2.setpos(-500, 0)
            racer_2.color(self.color)
            racer_2.speed(self.speed)
            racer_2.shapesize(stretch_len = self.size, stretch_wid = self.size)
            racer_2.showturtle() 

        if self.color == "green":
            racer_3.penup()
            racer_3.setpos(-500, -100)
            racer_3.color(self.color)
            racer_3.speed(self.speed)
            racer_3.shapesize(stretch_len = self.size, stretch_wid = self.size)
            racer_3.showturtle()

        if self.color == "red":
            racer_4.penup()
            racer_4.setpos(-500, 200)
            racer_4.color(self.color)
            racer_4.speed(self.speed)
            racer_4.shapesize(stretch_len = self.size, stretch_wid = self.size)
            racer_4.showturtle()

        if self.color == "grey":
            racer_5.penup()
            racer_5.setpos(-500, -200)
            racer_5.color(self.color)
            racer_5.speed(self.speed)
            racer_5.shapesize(stretch_len = self.size, stretch_wid = self.size)
            racer_5.showturtle()

    def movement(self, racer_1, racer_2, racer_3, racer_4, racer_5):

        if self.state == 0:
            
            while self.energy > 0:
                self.energy -= 1 #random.randint(15, 100)
                drunkness = random.randint(10, 90)
                choice = random.choice([1,2])
                if choice == 1:
                    racer_1.right(drunkness)
                else:
                    racer_1.left(drunkness)
                racer_1.forward(10)
                continue

        if self.state == 1:
            
            while self.energy > 0:
                self.energy -= 1 #random.randint(15, 100)
                drunkness = random.randint(10, 90)
                choice = random.choice([1,2])
                if choice == 1:
                    racer_2.right(drunkness)
                else:
                    racer_2.left(drunkness)
                racer_2.forward(10)
                continue

        if self.state == 2:
            
            while self.energy > 0:
                self.energy -= 1 #random.randint(15, 100)
                drunkness = random.randint(10, 90)
                choice = random.choice([1,2])
                if choice == 1:
                    racer_3.right(drunkness)
                else:
                    racer_3.left(drunkness)
                racer_3.forward(10)
                continue

        if self.state == 3:
            
            while self.energy > 0:
                self.energy -= 1 #random.randint(15, 100)
                drunkness = random.randint(10, 90)
                choice = random.choice([1,2])
                if choice == 1:
                    racer_4.right(drunkness)
                else:
                    racer_4.left(drunkness)
                racer_4.forward(10)
                continue

        if self.state == 4:
            
            while self.energy > 0:
                self.energy -= 1 #random.randint(15, 100)
                drunkness = random.randint(10, 90)
                choice = random.choice([1,2])
                if choice == 1:
                    racer_5.right(drunkness)
                else:
                    racer_5.left(drunkness)
                racer_5.forward(10)
                continue

normal_turtle = DefineTurtle("blue", 6, 1, 100, 0)
large_turtle = DefineTurtle("black", 3, 3, 150, 1)
drunk_turtle = DefineTurtle("green", 8, 1, 100, 2)
ninja_turtle = DefineTurtle("red", 10, 2, 200, 3)
giga_turtle = DefineTurtle("grey", 10, 3, 300, 4)

# normal_turtle.placement()
# large_turtle.placement()
# drunk_turtle.placement()
# ninja_turtle.placement()
# giga_turtle.placement()

# normal_turtle.movement()
# large_turtle.movement()
# drunk_turtle.movement()
# ninja_turtle.movement()
# giga_turtle.movement()


window.mainloop()