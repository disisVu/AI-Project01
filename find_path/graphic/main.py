from drawtable import draw_table
from readfile import read_file
import numpy as np
import turtle

# Read input from file
cols, rows, array = read_file('Turtle\input.txt')

# Draw table
turtle.screensize(canvwidth=6000, canvheight=4000, bg='#dddddd')
draw_table(cols, rows, array)