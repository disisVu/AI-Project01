from typing import Tuple
from drawtable import draw_table
from readfile import read_file
from polygon import is_list_of_convex
import turtle
import sys

def main():
    # Variables
    option = 0
    depth = 0

    # Read input from file
    cols, rows, array = read_file('input.txt')

    # Check if input are all convex polygons
    if is_list_of_convex(array[2:]) == False:
        print('\nError: at least one of given polygons is not convex.\n')
        return

    # Menu
    print('\nSearch algorithms:')
    print('1.  Breadth-first Search')
    print('2.  Uniform-cost Search')
    print('3.  Iterative Deepening Search')
    print('4.  Greedy Best-first Search')
    print('5.  A* Search')
    print('0.  Exit program')

    # User option
    while True:
        print()
        option = int(input('Input option: '))
        if 0 <= option <= 5:
            break;

    if option == 0:
        sys.exit()

    # Input IDS depth
    if option == 3:
        while True:
            print()
            depth = int(input('Input depth: '))
            if depth > 0:
                break;

    # Draw table
    turtle.screensize(canvwidth=6000, canvheight=4000, bg='#f3f3f3')
    draw_table(cols, rows, array, option, depth)

if __name__ == '__main__':
    main()