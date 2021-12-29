"""All the graphical things of tic tac toe"""
import turtle
import math

manu = turtle.Turtle()
manu.hideturtle()
manu.speed(0)
manu.pensize(3)


def go_home():
    """Resets the turtle to its original state"""
    manu.penup()
    manu.goto(0, 0)
    manu.pendown()
    manu.setheading(90)
    manu.penup()


def l_part(length, direction):
    """Draws the basic structural unit of a grid shaped like the
    letter L"""
    manu.forward(length)
    if direction == "left":
        manu.left(90)
    else:
        manu.right(90)
    manu.forward(length / 3)


def part_grid(length):
    """Draws three columns or rows"""
    l_part(length, "right")
    manu.right(90)
    l_part(length, "left")
    manu.left(90)
    l_part(length, "right")
    manu.right(90)
    manu.forward(length)


def grid(length):
    """Draws the tic tac toe grid"""
    manu.reset()
    manu.hideturtle()
    manu.speed(0)
    manu.pensize(3)
    manu.penup()
    manu.goto(int(-0.5 * length), int(0.5 * length))
    manu.pendown()
    part_grid(length)
    manu.right(90)
    part_grid(length)
    go_home()


def cross(size):
    """A cross"""
    manu.right(45)
    manu.forward(size)
    manu.penup()
    manu.right(135)
    manu.forward(size / math.sqrt(2))
    manu.right(135)
    manu.pendown()
    manu.forward(size)


def box_mark_cross(pos, size, grid_length):
    """Crosses out a box on the grid"""
    go_home()

    coords = {-grid_length: ["l", "b"], 0: ["c", "m"], grid_length: ["r", "t"]}
    x_coords = [coord[0] for coord in list(coords.values())]
    y_coords = [coord[1] for coord in list(coords.values())]
    terms = list(coords.keys())

    for i in pos:
        if i in x_coords:
            x_coord = terms[x_coords.index(i)] / 3 - size / (2 * math.sqrt(2))
        elif i in y_coords:
            y_coord = terms[y_coords.index(i)] / 3 - size / (2 * math.sqrt(2))

    # drawing
    try:
        manu.goto(x_coord, y_coord)
        manu.pendown()
        cross(size)
    except UnboundLocalError:
        print("Wrong input")


def box_mark_circle(pos, size, grid_length):
    """Circles a box on the grid"""
    go_home()

    coords = {-grid_length: ["l", "b"], 0: ["c", "m"], grid_length: ["r", "t"]}
    x_coords = [coord[0] for coord in list(coords.values())]
    y_coords = [coord[1] for coord in list(coords.values())]
    terms = list(coords.keys())

    for i in pos:
        if i in x_coords:
            x_coord = terms[x_coords.index(i)] / 3 + size / 2.2
        elif i in y_coords:
            y_coord = terms[y_coords.index(i)] / 3

    try:
        manu.goto(x_coord, y_coord)
        manu.pendown()
        manu.circle(size / 2.2)
    except UnboundLocalError:
        print("Wrong input")

