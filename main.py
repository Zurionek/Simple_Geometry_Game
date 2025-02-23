"""Geometry Game - check whether point with given parameters is inside the randomly generated rectangle.
Additional feature of the game - guessing the area of generated rectangle and graphical
presentation of the rectangle and the point generated by the by the user."""
from random import randint
import turtle

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
        and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area (self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)

class GuiRectangle(Rectangle):

    def draw (self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.x)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


#Create rectangle object
test_rectangle = GuiRectangle(Point(randint(0,400), randint(0,400)),
                           Point(randint(10, 400), randint(10, 400)))

#Print rectangle coordinates
print("Test Rectangle Coordinates: ",
      test_rectangle.point1.x, ",",
      test_rectangle.point1.y, "and",
      test_rectangle.point2.x, ",",
      test_rectangle.point2.y)

#Get point and area from user
user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

#Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(test_rectangle))
print("Your area guess was off by: ", test_rectangle.area() - user_area)
print("Correct area of the given rectangle is: {}.".format(test_rectangle.area()))

#Drawing the rectangle
myturtle = turtle.Turtle()
test_rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()