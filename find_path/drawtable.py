from asyncore import write
from ctypes.wintypes import RGB
from drawedge import draw_edge
import Search as search
import turtle
import numpy as np

# Global variables
cell_height = 40
cell_width = cell_height * 1.3
font_size = int(cell_height * 0.3)
zero_x = 0
zero_y = 0

# Colors
red1 = '#ff0000'
red2 = '#8b0000'
red3 = '#f97c7c'
red4 = '#ee6969'
yellow1 = '#ffff00'
yellow2 = '#9b870c'
yellow3 = '#e5cb69'
yellow4 = '#d8b324'
green1 = '#00ff00'
green2 = '#006400'
green3 = '#c8e1cc'
green4 = '#b8d8be'
blue1 = '#0000ff'
blue2 = '#011f4b'
blue3 = '#0099ff'
blue4 = '#005b96'

color = [red1, red2, yellow1, yellow2, green1, green2, blue3, blue4]

# Init turtle
t = turtle.Turtle()

# Remember turtle angle & position
# References: https://stackoverflow.com/questions/19126254/how-to-make-turtle-remember-its-position-in-l-systems
def get_turtle_state(turtle):
    # Return turtle's current heading and position.
    return turtle.heading(), turtle.position()

def restore_turtle_state(turtle, state):
    # Set the turtle's heading and position to the given values.
    turtle.penup()
    turtle.setheading(state[0])
    turtle.setposition(state[1][0], state[1][1])
    turtle.pendown()


# Self written code
def draw_line(length, delta):
    t.pendown()
    t.fd(length)
    t.penup()
    t.bk(length)
    t.lt(90)
    t.fd(delta)
    t.rt(90)

def draw_table(cols, rows, array, option, depth):
    # Maze number of columns and rows
    maze_columns = cols
    maze_rows = rows

    # Maze sizes
    maze_width = cell_width * (maze_columns + 1)
    maze_height = cell_height * (maze_rows + 1)

    # Calculate the 0 coordinate
    global zero_x
    global zero_y
    zero_x = (0 - maze_width) / 2
    zero_y = (0 - maze_height) / 2

    # Starting point:
    t.penup()
    t.setpos(zero_x, zero_y)
    t.speed(0)
    t.width(1)
    t.pencolor('#666666')

    # Save turtle state at the 0 coordinate
    begin_state = get_turtle_state(t)

    # Fill whole area gray
    t.fillcolor('#555555')
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

    # Declare start and goal cells
    start = [array[0][0], array[0][1]]
    goal = [array[0][2], array[0][3]]

    # Draw start
    restore_turtle_state(t, begin_state)
    fill_color_cell(start[0], start[1], blue3)
    restore_turtle_state(t, begin_state)
    write_cell(start[0], start[1], 'S', font_size, 'white')

    # Draw goal
    restore_turtle_state(t, begin_state)
    fill_color_cell(goal[0], goal[1], blue3)
    restore_turtle_state(t, begin_state)
    write_cell(goal[0], goal[1], 'G', font_size, 'white')

    # Init matrix map
    t.pencolor('#333333')
    matrix_map = init_map(cols, rows, array)

    # Draw obstacles
    t.pencolor('#333333')
    restore_turtle_state(t, begin_state)
    draw_obstacle(matrix_map, begin_state)

    # Reposition
    restore_turtle_state(t, begin_state)

    # Draw x-axis lines
    for i in range(maze_rows + 2):
        draw_line(maze_width, cell_height)

    # Reposition
    t.rt(90)
    t.fd(cell_height)

    # Draw y-axis lines
    for i in range(maze_columns + 2):
        draw_line(maze_height, cell_width)

    # Numbers on x-axis
    restore_turtle_state(t, begin_state)
    for i in range(maze_columns + 1):
        t.pendown()
        write_cell(i, -1, i, font_size, 'black')
        t.penup()

    # Numbers on y-axis
    restore_turtle_state(t, begin_state)
    for i in range(maze_rows + 1):
        t.pendown()
        write_cell(-1, i, i, font_size, 'black')
        t.penup()

    # Reposition
    restore_turtle_state(t, begin_state)

    # Calculate expanded nodes and path
    if option == 1:

        expanded_nodes = search.BFS(start, goal, np.flipud(matrix_map))
        path = search.RealReturnedPath(goal, expanded_nodes)
        # Expanded nodes mapping
        expanded_nodes_graphic = search.BFS([start[1], start[0]], [goal[1], goal[0]], np.rot90(matrix_map))

    elif option == 2:

        expanded_nodes = search.UCS(start, goal, np.flipud(matrix_map))
        path = search.RealReturnedPath(goal, expanded_nodes)
        expanded_nodes_graphic = search.UCS([start[1], start[0]], [goal[1], goal[0]], np.rot90(matrix_map))

    elif option == 3:

        expanded_nodes = search.IDS(start, goal, np.flipud(matrix_map), depth)
        path = search.RealReturnedPath(goal, expanded_nodes)
        expanded_nodes_graphic = search.IDS([start[1], start[0]], [goal[1], goal[0]], np.rot90(matrix_map), depth)

    elif option == 4:

        expanded_nodes = search.GBFS(start, goal, np.flipud(matrix_map))
        path = search.RealReturnedPath(goal, expanded_nodes)
        expanded_nodes_graphic = search.GBFS([start[1], start[0]], [goal[1], goal[0]], np.rot90(matrix_map))

    elif option == 5:

        expanded_nodes = search.A_star(start, goal, np.flipud(matrix_map))
        path = search.RealReturnedPath(goal, expanded_nodes)
        expanded_nodes_graphic = search.A_star([start[1], start[0]], [goal[1], goal[0]], np.rot90(matrix_map))

    # Remove start and goal
    expanded_nodes_graphic.remove([start[1], start[0]])
    if expanded_nodes_graphic.count([goal[1], goal[0]]) > 0:
        expanded_nodes_graphic.remove([goal[1], goal[0]])

    # Draw expanded nodes
    restore_turtle_state(t, begin_state)
    for i in range(len(expanded_nodes_graphic)):
        fill_color_cell(expanded_nodes_graphic[i][1], expanded_nodes_graphic[i][0], '#D3D3D3')

    # Draw path
    restore_turtle_state(t, begin_state)
    # If path is not empty
    if len(path) > 0:
        path.pop(len(path) - 1)
        path.pop(0)
        np.flip(path, axis=None)
        for i in range(len(path)):
            write_cell(path[i][0], path[i][1], '+', int(font_size * 1.2), 'black')

    # Result information
    write_cell(0, rows + 1.8, 'Cost of expanded nodes: ' + str(len(expanded_nodes)), int(font_size * 1.1), 'black')
    write_cell(0, rows + 1, 'Cost of final path: ' + str(len(path)), int(font_size * 1.1), 'black')

    # Hide turtle & Keep window open
    t.hideturtle()
    turtle.Screen().exitonclick()

def write_cell(x, y, content, font_size, color):
    t.pencolor(color)
    t.penup()
    t.setpos(zero_x + cell_width * (x + 0.5) - font_size / 4, zero_y + cell_height * (y + 0.5) - font_size / 1.5)
    t.pendown()
    t.write(content, font = ('Arial', font_size, 'bold'))

def fill_color_cell(x, y, color):
    t.penup()
    t.setpos(zero_x + cell_width * x, zero_y + cell_height * y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.fd(cell_width)
    t.lt(90)
    t.fd(cell_height)
    t.lt(90)
    t.fd(cell_width)
    t.lt(90)
    t.fd(cell_height)
    t.end_fill()
    t.lt(90)

# Init matrix map
def init_map(cols, rows, array):
    matrix = np.zeros((rows, cols))
    # Mark obstacle wall
    for j in range(2, len(array)):
        value = int((j - 2) * 2)
        n = len(array[j])
        q = n - 2
        for i in range(int(n / 2)):
            draw_edge(matrix, array[j][i*2], array[j][i*2 + 1], array[j][i*2 - q], array[j][i*2 + 1 - q], value, True)
    return matrix

# Fill color obstacle wall
def draw_obstacle(matrix, begin_state):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                fill_color_cell(j, i, color[int(matrix[i][j]) - 1])