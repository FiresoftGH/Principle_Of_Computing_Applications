import turtle

screen = turtle.Screen()
screen.setup(500, 500)

clock = turtle.Turtle()
clock.color('Green')
clock.width(4)

def hour_hand():
    clock.penup()
    clock.home()
    clock.right(90)

clock_label_count = 0

for i in range(12):
    clock_label_count += 1
    clock.penup()
    clock.setheading(-30 * (i + 3) + 75) #Turn the pen around
    clock.forward(22)
    clock.pendown()
    clock.forward(15)
    clock.penup()
    clock.forward(20)
    clock.write(str(clock_label_count), align="center", font=("Arial", 12, "normal"))

clock.setpos(2, -112)
clock.pendown()
clock.width(2)