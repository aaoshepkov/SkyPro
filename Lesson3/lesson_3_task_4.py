from turtle import *
t = Turtle()
# t.screen.setup(800, 800)
# def sq_cr(side):
#     t.circle(side / 2, 360)
#     t.left(180)
#     t.circle(side / 3, 360)
#     t.right(90)
# sq_cr(300)
# t.screen.exitonclick()
# t.screen.mainloop()


t.screen.setup(1400, 1200)
def sq_cr(side):
     t.circle(side / 3, 360)
     t.left(180)
     t.circle(side / 2, 360)
     t.right(90)
     t.penup(200)
     t.setposition([240, 320], None, None)
sq_cr(300)
t.screen.exitonclick()
t.screen.mainloop()