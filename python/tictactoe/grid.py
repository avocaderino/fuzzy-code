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
    """
    Draws the basic structural unit of a grid shaped like the
    letter "L"
    """
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
    # drawing a cross
    # specifying the y coordinate
    if "t" in list(pos):
        y_coord = grid_length / 3 - size / (2 * math.sqrt(2))
    elif "m" in list(pos):
        y_coord = -size / (2 * math.sqrt(2))
    elif "b" in list(pos):
        y_coord = -grid_length / 3 - size / (2 * math.sqrt(2))
    else:
        raise ValueError

    # specifying the x coordinate
    if "l" in list(pos):
        x_coord = -grid_length / 3 - size / (2 * math.sqrt(2))
    elif "c" in list(pos):
        x_coord = -size / (2 * math.sqrt(2))
    elif "r" in list(pos):
        x_coord = grid_length / 3 - size / (2 * math.sqrt(2))
    else:
        raise ValueError
    # drawing
    manu.goto(x_coord, y_coord)
    manu.pendown()
    cross(size)


def box_mark_circle(pos, size, grid_length):
    """Circles a box on the grid"""
    go_home()
    # drawing a circle
    rad = size / 2.2
    # specifying the y coordinate
    if "t" in list(pos):
        y_coord = grid_length / 3
    elif "m" in list(pos):
        y_coord = 0
    elif "b" in list(pos):
        y_coord = -grid_length / 3
    else:
        raise ValueError

    # specifying the x coordinate
    if "l" in list(pos):
        x_coord = -grid_length / 3 + rad
    elif "c" in list(pos):
        x_coord = rad
    elif "r" in list(pos):
        x_coord = grid_length / 3 + rad
    else:
        raise ValueError
    # drawing
    manu.goto(x_coord, y_coord)
    manu.pendown()
    manu.circle(rad)
