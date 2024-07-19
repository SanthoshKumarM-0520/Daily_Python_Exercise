import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
color_list=[(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

tim=Turtle()


def ten_dots():
    count=0
    while count!=10:

        tim.forward(50)
        random1=random.choice(color_list)
        tim.color(random1)
        tim.dot(20)
        count+=1
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0.0)



tim.penup()
tim.hideturtle()
tim.setheading(220)
tim.forward(300)
tim.setheading(0.0)
for i in range (10):
    ten_dots()




screen=Screen()
screen.exitonclick()