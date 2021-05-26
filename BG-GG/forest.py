import math, time, random, turtle


def map(n, start1, stop1, start2, stop2):
    return((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2


branchlimit = 10


def branch(pen, lengthrange, branchrange):
    global branchlimit
    length = random.randrange(round(lengthrange[0]), round(lengthrange[1]))
    branchamount = random.randrange(branchrange[0], branchrange[1])
    total_angle = branchamount*10+30 + random.randrange(1, 15) - 5
    partial_angle = total_angle / (branchamount-1)
    shorter = map(random.random(), 0, 1, 0.5, 0.9)
    lengthrange = (lengthrange[0] * shorter, lengthrange[1] * shorter)
    if length < branchlimit:
        return

    pen.pensize(math.ceil(length/15))
    pen.forward(length)
    pen.left(total_angle/2)
    branch(pen, lengthrange, branchrange)
    for _ in range(branchamount-1):
        pen.right(partial_angle)
        branch(pen, lengthrange, branchrange)
    pen.left(total_angle/2)
    pen.backward(length)


def floor(t, windowwidth, windowheight, height, color, treeamount):
    global branchrange, lengthrange
    t.setheading(90)
    t.penup()
    t.backward(windowheight/2 - height)
    t.setheading(180)
    t.backward(windowwidth/2)
    t.pendown()
    dist = windowwidth/treeamount
    treecolor = (0.6, 0.6, 0.6)
    planetcolor = color
    t.color(planetcolor)
    t.forward(dist/2)
    t.right(90)
    t.color(treecolor)
    branch(t, lengthrange, branchrange)
    t.left(90)
    for _ in range(treeamount):
        t.color(planetcolor)
        t.forward(dist)
        t.right(90)
        t.color(treecolor)
        branch(pen, lengthrange, branchrange)
        t.left(90)
        turtle.update()
    t.color(planetcolor)
    t.forward(dist/2)




lengthrange = (100, 130)
branchrange = (2, 5)
turtle.Screen().bgcolor('black')
for _ in range(100):
    pen = turtle.Turtle()
    pen.color('white')
    turtle.tracer(0, 0)
    screenwidth = turtle.Screen().window_width()
    screenheigth = turtle.Screen().window_height()
    color = 'white'
    treeamount = 4
    heigth = 100
    floor(pen, screenwidth, screenheigth, heigth, color, treeamount)
    turtle.update()
    time.sleep(10)
    pen.clear()

time.sleep(20)
