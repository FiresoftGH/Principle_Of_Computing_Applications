import turtle
from threaded_turtle import ThreadSerializer, TurtleThread

ctrl = ThreadSerializer()                        ## <-- create a serializer

t1=turtle.Turtle()
t2=turtle.Turtle()

def tes1(t1):                                    ## <-- additional argument
  t1.speed(0)
  i=0
  while i < 360:
    t1.forward(1)
    t1.left(1)
    i+=1

def tes2(t2):                                    ## <-- additional argument
  t2.speed(0)
  i=0
  while i < 360:
    t2.forward(1)
    t2.right(1)
    i+=1

t = TurtleThread(ctrl, t1, target=tes1)          ## <-- additional arguments
t.daemon = True
t.start()

t3 = TurtleThread(ctrl, t2, target=tes2)         ## <-- additional arguments
t3.daemon = True
t3.start()

ctrl.run_forever(1)    