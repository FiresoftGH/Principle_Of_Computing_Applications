import turtle
data = []
turtle.penup()

def stars1(n):
    if n > 0:
        stars = ""
        for x in range(n):
            stars += "*"
            turtle.dot(10, "black")
            turtle.fd(20)
        turtle.goto(0, turtle.ycor())
        turtle.right(90)
        turtle.fd(20)
        turtle.right(-90)
        print(stars)
        data.append(stars)
        # print(data)
        stars1(n - 1)
    else:
        data.reverse()
        for x in data:
            print(x)
            for x in range(len(x)): 
                turtle.dot(10, "black")
                turtle.fd(20)
            turtle.goto(0, turtle.ycor())
            turtle.right(90)
            turtle.fd(20)
            turtle.right(-90)
        
# stars1(5)
convert = {}
data_2 = []

def stars2(n):
    if n > 0:
        for x in range(n):
            val += 1
        return
        
stars2(5)

turtle.mainloop()