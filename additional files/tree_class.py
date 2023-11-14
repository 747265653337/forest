import random, turtle, time
from blum_blum_shub import BlumBlumShub
from map import map


class Tree():
    def __init__(self, pos, size):
        self.pen = turtle.Turtle()
        self.BBS = BlumBlumShub(64)
        self.seed = self.BBS.seed
        self.limit = 10
        # setup randomranges depending on tree size
        self.branchrange = (3, 5)
        self.lengthrange = (size//3, size//1.5)
        self.anglerange = (60, 100)
        self.shorter = 0.75
        # setup turtle
        t = self.pen
        t.ht()
        y = turtle.Screen().window_height()
        val = abs((pos[1]-y/2)/y)*0.7
        color = (val, val, val)
        t.color(color)
        t.setheading(90)
        t.penup()
        t.goto(pos)
        t.pendown()

    #  create a stem fznction to create the first branch, to have a bigger difference between stem and branches
    def stem(self, lengthrange):
        length = lengthrange[1]
        branchamount = self.BBS.state % (self.branchrange[1] - self.branchrange[0]) + self.branchrange[0]
        totalangle = self.BBS.state % (self.anglerange[1] - self.anglerange[0]) + self.anglerange[0]
        lengthrange = (lengthrange[0] * (self.shorter**3), lengthrange[1] * self.shorter)
        turnangle = totalangle/(branchamount-1)  # poles and fences

        self.pen.pensize(length // 10)
        self.pen.forward(length)
        self.pen.left(totalangle/2)
        self.branch(lengthrange)
        for _ in range(branchamount-1):
            self.pen.pensize(length // 10)
            self.pen.right(turnangle)
            self.branch(lengthrange)
        self.pen.left(totalangle/2)
        self.pen.backward(length)

    def branch(self, lengthrange, step=0):
        length = self.BBS.nextpseudorand() % (lengthrange[1] - lengthrange[0]) + lengthrange[0]
        if length < self.limit:
            return
        branchamount = self.BBS.state % (self.branchrange[1] - self.branchrange[0]) + self.branchrange[0]
        totalangle = self.BBS.state % (self.anglerange[1] - self.anglerange[0]) + self.anglerange[0]
        turnangle = totalangle/(branchamount-1)  # poles and fences
        lengthrange = (lengthrange[0]*self.shorter, lengthrange[1]*self.shorter)
        step += 1

        self.pen.pensize(1 / step * 8)
        self.pen.forward(length)
        self.pen.left(totalangle/2)
        self.branch(lengthrange, step)
        for _ in range(branchamount-1):
            self.pen.pensize(length // 10)
            self.pen.right(turnangle)
            self.branch(lengthrange, step)
        self.pen.left(totalangle/2)
        self.pen.backward(length)


turtle.tracer(0, 0)
turtle.Screen().bgcolor('black')
trees = []
positions = []
x = turtle.Screen().window_width()
y = turtle.Screen().window_height()
for _ in range(37):
    pos = (random.randrange(-x//2, x//2),random.randrange(-y//2, y//2))
    positions.append(pos)
print(positions)
for i in range(0, len(positions)):
    for j in range(i+1, len(positions)):
        if positions[i][1] < positions[j][1]:
            positions[i], positions[j] = positions[j], positions[i]
print(positions)
for pos in positions:
    size = 140 - (pos[1] + (y//2))/y * 40
    trees.append(Tree(pos, size))
for tree in trees:
    tree.stem(tree.lengthrange)
    turtle.update()
    print('drawn tree')
print('done')
'''
test2 = Tree((0, -150), 200)
print(test2.seed)
for frame in range(100):
    test2.stem(test2.lengthrange)
    test2.BBS.state = test2.seed
    turtle.update()
    test2.pen.clear()
    print(frame)
'''
turtle.done()