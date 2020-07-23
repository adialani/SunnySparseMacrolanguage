import turtle
import math
s = turtle.Screen()
s.bgcolor("blue")

t = turtle.Turtle()
t.shape("turtle")  # the other shape are "arrow", "turtle", "circle", "square", "triangle", "classic"
t.color("#30ffee")  # you can input the hex number, web color name, or RGV value
t.speed(0)          # 0 is the fastest speed 1-10 are animated speeds 1 iis the slowest 10 is the fastest
t.pensize(2)        # size of the line

#how to move the shape
t.penup()
t.goto(100,100)
t.pendown()

def square(size):
	for i in range(4):
		t.fd(size)
		t.rt(90)


def triangle(size):
	for i in range(3):
		t.fd(size)
		t.lt(120)


def house(size):
	square(size)
	triangle(size)


t.penup()
t.goto(0,0)
t.pendown()

def house(size):   
	square(size)
	triangle(size)      #house(100)


def squares(size):
	while size > 0:
		square(size)
		t.penup()
		t.rt(3)
		t.fd(10/math.sqrt(2))
		t.lt(0)
		t.rt(0)
		t.pendown()
		size -= 7
#squares(200)

def circle(size):
	for i in range(35):
		t.rt(10)
		t.fd(10)

def shape(sides, size):
	for i in range(sides):
		t.fd(size)
		t.rt(360.0/sides)      
#shape(sides =5, size = 36)

def shapes(sides, size):
	while size > 0:
		shape(sides, size)
		t.penup()
		t.rt(90)
		t.fd(10)
		t.lt(90)
		t.rt(2.5)
		t.pendown()
		size -= 1   
#shapes(100,7)


def spiro(sides, size, steps, degrees):
	for i in range(360//degrees):
		shape(sides, size)
		t.fd(steps)
		t.rt(degrees)
#spiro(sides = 12, size = 50, steps = 20, degrees = 360/10)


def spiral(nlines, degrees, increase):
	steps = 1
	for i in range(nlines):
		t.fd(steps)
		t.rt(degrees)
		steps += increase
#spiral(5000, 21, 0.1)
#spiral (500, 121, 3)

def sphere(size)
	shade = 75
	t.color(0,0,shade)
	while size > 0
		t.begin_fill()
		shape(30, size)	