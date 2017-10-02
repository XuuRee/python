"""
uco: 433439
jmeno: Filip Valchar
hw: 1
"""

from turtle import Turtle, clear


# first task, alternating multiples
def alternating_multiples(n):
    if (n != 0):
        alternating = 0
        for i in range(0, n * 11, n):
            if (alternating % 2 == 1):
                i *= -1
            print(i, end=" ")
            alternating += 1
        print()


# second task, crossing
def crossing(n, length):
    if (n != 0):
        rows = 2 * n + 1
        cols = length + 2
        for i in range(rows):
            for j in range(cols):
                if (i % 2 == 0 or (j < 1 or j > length)):
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()


# third task, mocniny
def mocniny(m, n):
    # header (from seminar last week)
    print(" ", " ", end=" ")
    for col in range(1, m + 1):
        print(col, end=" ")
    print()
    print(" ", " ", end=" ")
    for col in range(m):
        print("-", end=" ")
    print()

    # table with powers
    for i in range(1, n + 1):
        print(i, "|", end=" ")
        for j in range(1, m + 1):
            print(j ** i, end=" ")
        print()


# fourth task, castle
def square(side, julie):
    for i in range(4):
        julie.forward(side)
        julie.right(90)
    julie.forward(side)


def triangle(side, julie):
    for i in range(2):
        julie.left(120)
        julie.forward(side)
    julie.left(120)
    julie.forward(side)


# function castle is only for inputs with
# variable 'towers' bigger than two. Spaces
# (or squares in this case) can't be placed
# between one or zero towers.
# This is my interpretation of task :-)
def castle(towers, length, space):
    if (towers > 1):
        julie = Turtle()
        base = ((towers - 1) * space) + towers
        for i in range(base):
            square(length, julie)
            if (i % (space + 1) == 0):
                triangle(length, julie)
        julie.clear()


# fifth task, draw python
def draw_python():
    julie = Turtle()
    julie.right(25)
    julie.forward(10)
    julie.right(85)
    julie.forward(100)
    julie.left(110)
    julie.forward(140)
    julie.left(95)
    julie.forward(80)
    julie.right(40)
    julie.forward(20)
    julie.left(140)
    julie.forward(30)
    julie.left(65)
    julie.forward(45)
    julie.right(85)
    julie.forward(52)
    julie.right(90)
    julie.forward(76)
    julie.left(45)
    julie.forward(15)
    julie.left(68)
    julie.forward(30)
    julie.left(130)
    julie.forward(10)
    julie.left(130)
    julie.forward(8)
    julie.left(100)
    julie.forward(28)
    julie.left(70)
    julie.forward(20)
    julie.right(90)
    julie.forward(22)
    julie.left(180)
    julie.forward(48)
    julie.clear()


alternating_multiples(2)
alternating_multiples(3)
crossing(4, 8)
mocniny(5, 3)
castle(5, 50, 3)
draw_python()
