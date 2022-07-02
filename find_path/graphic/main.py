from drawtable import draw_table
from drawline import draw_line
from readfile import read_file
import numpy as np
import turtle

# Cell size
cell_height = 30
cell_width = cell_height * 1.3

# Read input from file
cols, rows, array = read_file('Turtle\input.txt')

# Draw table
turtle.screensize(canvwidth=6000, canvheight=4000, bg='white')
draw_table(cols, rows, array)