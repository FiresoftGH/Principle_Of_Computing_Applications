import turtle
window = turtle.Screen()
window.bgcolor("white")
window.setup(width = 600, height = 600)
window.title("Analog Clock")

clock = turtle.Turtle() # Object
clock.hideturtle()
clock.speed(0)
clock.pensize(3)

def clock_frame(draw, hour, minute, second):
    # Circle Frame
    draw.penup()
    draw.goto(0, 210)
    draw.setheading(180)
    draw.color("black")
    draw.pendown()
    draw.circle(210)

    # Draw the lines for the hour marks
    draw.penup()
    draw.goto(0,0)
    draw.setheading(90)

    for number_in_clock in range(12):
        draw.forward(190)
        draw.pendown()
        draw.forward(20)
        draw.penup()
        draw.goto(0, 0)
        draw.right(30)

    # Draw the hour hand
    draw.penup()
    draw.goto(0, 0)
    draw.color("red")
    draw.setheading(90)
    angle = (hour / 12) * 360
    angle += 0.5 * minute
    draw.rt(angle)
    draw.pendown()
    draw.forward(100)
    draw.stamp()

    # Draw the minute hand
    draw.penup()
    draw.goto(0, 0)
    draw.color("blue")
    draw.setheading(90)
    angle = (minute / 60) * 360
    angle += 0.1 * second
    draw.rt(angle)
    draw.pendown()
    draw.forward(150)
    draw.stamp()

    # Draw the second hand
    draw.penup()
    draw.goto(0, 0)
    draw.color("green")
    draw.setheading(90)
    angle = (second / 60) * 360
    draw.rt(angle)
    draw.pendown()
    draw.forward(170)
    draw.stamp()

hour = int(input("Hours: "))
if hour > 12:
    convert = hour - 12
minute = int(input("Minutes: "))
second = int(input("Seconds: "))

clock_frame(clock, hour, minute, second)

window.mainloop()