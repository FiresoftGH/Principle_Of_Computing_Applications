import turtle
debug = []
turtle.penup()

def stars1(n):
    if n > 1:
        stars = ""
        for x in range(n - 1):
            stars += "*"
            turtle.dot(10, "black")
            turtle.fd(20)
        turtle.goto(0, turtle.ycor())
        turtle.right(90)
        turtle.fd(20)
        turtle.right(-90)
        print(stars)
        debug.append(stars)
        # print(debug)
        stars1(n - 1)
    else:
        debug.reverse()
        for x in debug:
            print(x)
            for x in range(len(x)): 
                turtle.dot(10, "black")
                turtle.fd(20)
            turtle.goto(0, turtle.ycor())
            turtle.right(90)
            turtle.fd(20)
            turtle.right(-90)
        

stars1(5)
turtle.mainloop()
        