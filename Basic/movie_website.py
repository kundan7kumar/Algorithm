#Classes
import turtle
def draw_square():
    window=turtle.Screen()
    #create the turtle --Draw the Sqaure
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1,36):
        draw_square(brad)
        brad.right(10)
#     brad.forward(100)
#     brad.right(90)
#     brad.forward(100)
#     brad.right(90)
#     brad.forward(100)
#     brad.right(90)
#     brad.forward(100)
#     brad.right(90)
# #create the turtle--Draw Circle
#     angie=turtle.Turtle()
#     angie.shape("arrow")
#     angie.color("blue")
#     angie.circle(100)

    window.exitonclick ()

draw_square()

