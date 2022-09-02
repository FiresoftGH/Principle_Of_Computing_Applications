import turtle
debug = []

def control():
    turtle.dot(10, "black")
    turtle.penup()
    # turtle.left(180)
    turtle.forward(20)
    turtle.pendown()
    # turtle.left(-180)

def stars1(n):
    if n > 1:
        stars = ""
        for x in range(n - 1):
            stars += "*"
            control()
        print(stars)
        debug.append(stars)
        # print(debug)
        stars1(n - 1)
    else:
        debug.reverse()
        for x in debug:
            print(x)
        

stars1(5)
turtle.mainloop()
        