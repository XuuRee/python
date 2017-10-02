"""
uco: 433439
jmeno: Filip Valchar
hw: 1
"""

from turtle import Turtle, done, clear

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

"""
alternating_multiples(0)
alternating_multiples(-2)
alternating_multiples(1)
alternating_multiples(2)
alternating_multiples(3)
alternating_multiples(4)
alternating_multiples(5)
alternating_multiples(6)
alternating_multiples(7)
alternating_multiples(8)
alternating_multiples(9)
alternating_multiples(10)
alternating_multiples(11)
"""


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

"""
crossing(0, 0)
crossing(1, 0)
crossing(1, 1)
crossing(1, 2)
crossing(4, 8)
crossing(3, 10)
"""


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

"""
mocniny(0, 3)
mocniny(1, 3)
mocniny(4, 0)
mocniny(2, 3)
mocniny(5, 3)
mocniny(8, 3)
"""


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

# vzhledem k tomu, ze zadani mluvilo o poctu vezi
# a _mezer_ mezi nimi, neresil jsem situaci kdy
# by na vstupu bylo zadana jedna nebo nula vezi. 
def castle(towers, length, space):
    julie = Turtle()
    base = ((towers - 1) * space) + towers
    for i in range(base):
        square(length, julie)
        if (i % (space + 1) == 0):
           triangle(length, julie)
    julie.clear()

"""
castle(5, 35, 0)
castle(5, 35, 1)
castle(5, 35, 2)
castle(5, 35, 3)
castle(2, 35, 4)
"""


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

"""
draw_python()
"""
