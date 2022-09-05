import turtle

turtle.reset()
turtle.shape("turtle")
turtle.color("green")
turtle.speed(10)
turtle.goto(-100, 0)
turtle.lt(360)
# turtle.seth(90)
 

def draw(size): 
    if size < 10: # Base Case
        return
    else: # Recursion Case
        turtle.fd(size)
        turtle.lt(30)
        draw(size * 0.6) # Calls the function after turning left
        turtle.rt(60)
        draw(size * 0.6) #Calls the function after turning right
        turtle.lt(30)
        turtle.bk(size)
        return

draw(200)

turtle.mainloop()