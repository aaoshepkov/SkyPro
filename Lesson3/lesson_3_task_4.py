from turtle import *
t = Turtle()
t.screen.setup(800, 800)
def sq_cr(side):
    t.circle(side / 2, 360)
    t.left(180)
    t.circle(side / 3, 360)
    t.right(90)
sq_cr(300)
t.screen.exitonclick()
t.screen.mainloop()