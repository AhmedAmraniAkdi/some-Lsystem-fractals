from turtle import *


# expands the sequence as in wikipedia, the order is the depth,  the axiom is the start
# and follows the rules, care, the indices of a variable and her rule in the list have to be the same
# for example: [X, Y] -> [XX, YY] means X follows the rule XX and Y follows YY!

def expand(order, axiom, variables, rules):
    """ axiom is string
    variables and rules are list of strings
    """
    expansion = ""
    if order == 0:
        return list(axiom)
    for variable in list(axiom):
        expansion += rules[variables.index(variable)]
    return expand(order - 1, expansion, variables, rules)


# Some coloring functions.

def rainbow():
    colors_ = t.color()
    red_ = (colors_[0][0] + colors_[0][1]) % 255
    green_ = (colors_[0][1] + colors_[0][2]) % 255
    blue_ = (colors_[0][2] + colors_[0][0]) % 255
    t.pencolor((red_, green_, blue_))


def toBlue():
    colors_ = t.color()
    red_ = max(0, (colors_[0][0] - 2))
    green_ = max(0, (colors_[0][1] - 2))
    blue_ = min(255, (colors_[0][2] + 3))
    t.pencolor((red_, green_, blue_))


# The function that does the job!

def drawing(axiom, angle, distance):
    """ 0 and 1 for going forward, + for turning right and - for turning left,
    ] for pop the last directions/positions and [ for saving the current ones
    with push.
    """
    count = 0
    positions = []
    directions = []
    colorplan = []
    for variable in axiom:
        if count % 3 == 0: # every 3 steps change color
            # rainbow()
            toBlue()
        if variable == '0' or variable == '1': 
            t.forward(distance)
            count += 1 # add counting only when moving forward
        if variable == '[':
            positions.append(t.pos())
            directions.append(t.heading())
            colors_ = t.color()
            colorplan.append(colors_[0])
            # t.left(angle)
        if variable == ']':
            t.penup()
            t.setpos(positions.pop())
            t.setheading(directions.pop())
            t.pencolor(colorplan.pop())
            # t.right(angle)
            t.pendown()
        if variable == '-':
            t.left(angle)
        if variable == '+':
            t.right(angle)
    # t.getscreen().getcanvas().postscript(file="picture.eps") if you want to print image to postscript
    exitonclick()


# list1 = expand(8, "0", ["0", "1", "]", "["], ["1[0]0", "11", "]", "["]) # Fractal (binary) tree
# list2 = expand(10, "0X", ["X", "Y", "0", "+", "-"], ["X+Y0+", "-0X-Y", "0", "+", "-"]) # Dragon curve
list3 = expand(6, "X", ["X", "0", "+", "-", "]", "["], ["0[-X][X]0[-X]+0X", "00", "+", "-", "]", "["])  # Fractal plant
# list4 = expand(5, "X", ["X", "Y", "0", "+", "-", "]", "["], ["-Y0+X0X+0Y-", "+X0-Y0Y-0X+", "0", "+", "-", "]", "["]) # Hilbert curve

colormode(255)
bgcolor((0, 0, 0))
t = Turtle()
t.pen(pencolor=(255, 127, 80), shown=False, pendown=False, speed=0)
t.setpos(-165, -265)
t.pendown()
t.left(75)

drawing(list3, 25, 4)  # It is set to draw the fractal plant, mind the angles!
