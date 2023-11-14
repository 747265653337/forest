import turtle, math, random, time


def branch(t, length, branchamount, viewangle, shorteningfactor, limit):
    if length < limit:
        return
    t.pensize(length/15)
    t.forward(length)
    t.right(viewangle/2)
    turnangle = (viewangle/branchamount)
    for _ in range(branchamount):
        branch(t, length * shorteningfactor, branchamount, viewangle, shorteningfactor, limit)
        t.left(turnangle)
    branch(t, length * shorteningfactor, branchamount, viewangle, shorteningfactor, limit)
    t.right((turnangle*branchamount)-(viewangle/2))
    t.backward(length)


def floor(t, windowwidth, windowheight, height, color, treeamount):
    t.setheading(90)
    t.penup()
    t.backward(windowheight/2 - height)
    t.setheading(180)
    t.backward(windowwidth/2)
    t.pendown()
    dist = windowwidth/treeamount
    treecolor = 'white'
    planetcolor = color
    t.color(planetcolor)
    t.forward(dist/2)
    t.right(90)
    t.color(treecolor)
    branchamount = random.randint(2, 5)
    branchlength = random.randint(90, 110)
    branch(t, branchlength, branchamount, 90, 0.7, 5)
    t.left(90)
    for _ in range(treeamount):
        t.color(planetcolor)
        t.forward(dist)
        t.right(90)
        t.color(treecolor)
        branchamount = random.randint(2, 5)
        branchlength = random.randint(30, 100)
        branch(t, branchlength, branchamount, 90, 0.7, 5)
        t.left(90)
        turtle.update()
    t.color(planetcolor)
    t.forward(dist/2)

def planet(t, radius, color, treeamount):
    t.speed(0)
    t.penup()
    t.forward(radius)
    t.left(90)
    t.pendown()
    t.color(color)
    width = t.pensize()
    turnangle = 360/treeamount
    treecolor = (0.6, 0.6,0.6)
    planetcolor = (0.4, 0.4, 0.4)
    for i in range(treeamount):
        t.color(treecolor)
        t.pensize(width=3)
        t.circle(radius, turnangle)
        t.right(90)
        t.color(planetcolor)
        t.pensize(width=width)
        branchamount= random.randint(3, 5)
        branchlength = random.randint(40, 60)
        branch(t, branchlength, branchamount, 90, 0.7, 5)
        t.left(90)
        turtle.update()
    t.color(planetcolor)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw():
    turtle.Screen().setup(width=1.0, height=1.0)
    screenwidth = turtle.Screen().window_width()
    screenheigth = turtle.Screen().window_height()
    # turtle.Screen().setworldcoordinates(screenwidth/2, screenheigth/2)
    t = turtle.Turtle()
    turtle.tracer(0, 0)
    t.penup()
    t.setpos(0, 0)
    t.ht()
    t.pendown()
    t.color((1, 1, 1))
    planet(t, 100, 'green', 12)
    '''
    floor(t, screenwidth, screenheigth, 120, (0.4, 0.4, 0.4), 9)
    t.penup()
    t.setpos(0,0)
    t.penup()
    floor(t, screenwidth, screenheigth, 320, (0, 0, 0), 11)
    t.penup()
    t.setpos(0, 0)
    t.pendown()
    floor(t, screenwidth, screenheigth, 220, (0, 0, 0), 15)
    '''
    # t.setheading(90)
    # branch(t, 120, 4, 120, 0.7, 6)
    turtle.update()


if __name__ == '__main__':
    turtle.Screen().bgcolor((0, 0, 0))
    draw()
    print('done')
    turtle.done()
