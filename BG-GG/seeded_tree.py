import blum_blum_shub
import turtle
import map


def branch(blum_blum_shub_object, length, position=(0, 0), direction=90):
    if length < 20:
        return
    # setup
    pen = turtle.Turtle()
    pen.ht()
    turtle.tracer()
    pen.penup()
    pen.setposition(position)
    pen.pendown()
    pen.setheading(direction)

    # calc params
    modifier = map.map(
        (blum_blum_shub_object.nextpseudorand() % 100 / 100),
        0,
        99,
        0.7,
        0.9
    )
    length *= modifier
    width = length/10
    total_angle = map.map(
        ((blum_blum_shub_object.state % 10000 -
          (blum_blum_shub_object.nextpseudorand() % 100)) / 100),
        0,
        99,
        45,
        180)
    amnt_of_branches = round(map.map(
        ((blum_blum_shub_object.state % 1000000 -
          (blum_blum_shub_object.nextpseudorand() % 10000)) / 10000),
        0,
        99,
        1,
        4
    ))

    # draw branch
    pen.pensize(width)
    pen.fd(length)
    pen.right(total_angle/2)
    branch(blum_blum_shub_object, length, pen.position(), pen.heading())
    for _ in range(amnt_of_branches):
        pen.left(total_angle/(amnt_of_branches+1))
        branch(blum_blum_shub_object, length, pen.position(), pen.heading())


branch(blum_blum_shub.BlumBlumShub(seed=1097818482), 100)
turtle.update()

turtle.done()
