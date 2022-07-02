import turtle

# Init turtles
t = turtle.Turtle()

# Number font
font_size = 10

# Maze size
maze_columns = 20
maze_rows = 16

# Cell size
cell_height = 30
cell_width = cell_height * 1.3

# Maze dimensions
maze_width = cell_width * maze_columns
maze_height = cell_height * maze_rows

# Calculate the 0 coordinate
zero_x = (0 - maze_width) / 2
zero_y = (0 - maze_height) / 2

# Starting point:
t.penup()
t.setpos(zero_x, zero_y)
t.speed(0)
t.width(1)
t.pencolor('black')

# Fill whole area gray
t.fillcolor('gray')
t.begin_fill()
t.fd(maze_width)
t.lt(90)
t.fd(maze_height)
t.lt(90)
t.fd(maze_width)
t.lt(90)
t.fd(maze_height)
t.end_fill()

# Fill the middle area white
t.lt(180)
t.penup()
t.fd(cell_height)
t.rt(90)
t.fd(cell_width)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.fd(maze_width - cell_width * 2)
t.lt(90)
t.fd(maze_height - cell_height * 2)
t.lt(90)
t.fd(maze_width - cell_width * 2)
t.lt(90)
t.fd(maze_height - cell_height * 2)
t.end_fill()

# Reposition
t.penup()
t.setpos(zero_x, zero_y)
t.pendown()
t.lt(90)

# Draw line
def line(length, delta):
    t.pendown()
    t.fd(length)
    t.penup()
    t.bk(length)
    t.lt(90)
    t.fd(delta)
    t.rt(90)

# Draw x-axis lines
for i in range(maze_rows + 1):
    line(maze_width, cell_height)

# Reposition
t.rt(90)
t.fd(cell_height)

# Draw y-axis lines
for i in range(maze_columns + 1):
    line(maze_height, cell_width)

# Numbers on x-axis
t.setpos((zero_x - cell_height / 2 - font_size / 2), (zero_y - cell_height + font_size / 2))
t.lt(90)
t.pencolor('black')

for i in range(maze_columns + 1):
    t.pendown()
    t.write(i, font = ('Arial', font_size, 'bold'))
    t.penup()
    t.fd(cell_width)

# Numbers on y-axis
t.setpos((zero_x - cell_height / 2 - font_size / 2), (zero_y - cell_height + font_size / 2))
t.lt(90)
t.pencolor('black')

for i in range(maze_rows + 1):
    t.pendown()
    t.write(i, font = ('Arial', font_size, 'bold'))
    t.penup()
    t.fd(cell_height)

# Hide turtle & Keep window open
t.hideturtle()
turtle.Screen().exitonclick()