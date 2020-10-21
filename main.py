# This is a sample Python script.
from graphics import *

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def my_graphic():
    win = GraphWin()
    pt = Point(100,50)
    pt.draw(win)
    draw_circle(win, pt)
    draw_circle(win, pt)
    draw_rect(win, pt)
    win.getKey()  # Pause to view result
    win.close()


def draw_circle(win: GraphWin, pt: Point):
    cir = Circle(pt, 25)
    cir.draw(win)
    cir.setOutline('yellow')
    cir.setFill('orange')


def draw_line(win: GraphWin, pt: Point):
    line = Line(pt, Point(150, 100))
    line.draw(win)


def draw_rect(win: GraphWin, pt: Point):
    rect = Rectangle(Point(20, 10), pt)
    rect.draw(win)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    my_graphic()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
