# -*- coding: utf-8 -*-
from . import helpers
from graphics import *


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
        win = get_win()
        center_x = 1024 / 2
        center_y = 768 / 2
        cir = get_circle(100, Point(center_x, center_y))
        cir.setOutline('yellow')
        cir.setFill('orange')
        cir.draw(win)
        input("Press Enter to continue...")


def get_win():
    return GraphWin("My Graphics Window", 1024, 768)


def get_circle(radius, center):
    return Circle(center, radius)
