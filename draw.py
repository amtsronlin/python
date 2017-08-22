import turtle
t = turtle.Pen()
#-----Square
def square(side):
    for i in range(0,5):
        t.forward(side)
        t.left(90)
square(30)
square(50)
#----Circle
def circle(radius):
    t.circle(radius)
circle(30)
circle(50)
#------star
t.reset()
for i in range (1,38) :
    t.forward(100)
    t.left(175)
t.reset()
for i in range (1,20) :
    t.forward(100)
    t.left(96)
#-----up
t.up()
t.forward(250)
#-----teric
t.color(0,0,1)
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(30)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(90)
t.forward(70)
t.left(90)
t.forward(40)
t.left(90)
t.forward(30)
t.end_fill()
t.getscreen()._root.mainloop()


