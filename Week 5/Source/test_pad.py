import turtle

turtle.penup()
result = []
def stars2(n):
    if n > 0:
        
        answer = ""
        answer += "*"
        result.append(answer)
        for x in range(len(result)):
            turtle.dot(10, "black")
            turtle.fd(20)
        turtle.right(90)
        turtle.fd(20)
        turtle.goto(0, turtle.ycor())
        turtle.right(-90)
        print(''.join(result))
        stars2(n - 1)
    else:

        result.reverse()
        for x in range(len(result)):
            print(''.join(result))
            result.pop()
            for y in range(len(result) + 1):
                turtle.dot(10, "black")
                turtle.fd(20)
            turtle.right(90)
            turtle.fd(20)
            turtle.goto(0, turtle.ycor())
            turtle.right(-90)

stars2(5)

turtle.mainloop()