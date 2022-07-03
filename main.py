from drawtable import draw_table
from readfile import read_file
import turtle
import sys

# Variables
option = 0
depth = 0

# Read input from file
cols, rows, array = read_file('input.txt')

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