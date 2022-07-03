# MODULES
import pygame, sys
import numpy as np


# initializes pygame
pygame.init()

# ---------
# KHOI TAO BIEN
# ---------
WIDTH = 700
HEIGHT = 700
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
SQUARE_SIZE = 0
BOARD_ROWS = 0
BOARD_COLS = 0
CIRCLE_WIDTH = 10
CROSS_WIDTH = 10
# CHI SO MAU RGB
BG_COLOR = (9, 29, 69)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
# -----------------
# KHOI TAO MAN HINH
# -----------------
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BG_COLOR )

# ---------
# FUNCTIONS
# ---------
def boardRC(choose):
    if choose == 1:
        BOARD_ROWS = 3
        BOARD_COLS = 3
        SQUARE_SIZE = WIDTH / BOARD_ROWS
    if choose == 2:
        BOARD_ROWS = 5
        BOARD_COLS = 5
        SQUARE_SIZE = WIDTH / BOARD_ROWS
    if choose == 3:
        BOARD_ROWS = 7
        BOARD_COLS = 7
        SQUARE_SIZE = WIDTH / BOARD_ROWS
    return BOARD_ROWS, BOARD_COLS, SQUARE_SIZE
        
def draw_lines(choose):
    if choose == 1:
        # 1 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
        # 2 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )

        # 1 vertical
        pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
        # 2 vertical
        pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
    if choose == 2:
        # 1 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
        # 2 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )
        # 3 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, 3 * SQUARE_SIZE), (WIDTH, 3 * SQUARE_SIZE), LINE_WIDTH )
        # 4 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, 4 * SQUARE_SIZE), (WIDTH, 4 * SQUARE_SIZE), LINE_WIDTH )

        # 1 vertical
        pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
        # 2 vertical
        pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
        # 1 vertical
        pygame.draw.line( screen, LINE_COLOR, (3 * SQUARE_SIZE, 0), (3 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
        # 2 vertical
        pygame.draw.line( screen, LINE_COLOR, (4 * SQUARE_SIZE, 0), (4 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
    if choose == 3:
        # 1 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
        # 2 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )
        # 3 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, 3 * SQUARE_SIZE), (WIDTH, 3 * SQUARE_SIZE), LINE_WIDTH )
        # 4 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, 4 * SQUARE_SIZE), (WIDTH, 4 * SQUARE_SIZE), LINE_WIDTH )
        # 5 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, 5 * SQUARE_SIZE), (WIDTH, 5 * SQUARE_SIZE), LINE_WIDTH )
        # 6 horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, 6 * SQUARE_SIZE), (WIDTH, 6 * SQUARE_SIZE), LINE_WIDTH )

        # 1 vertical
        pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
        # 2 vertical
        pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
        # 3 vertical
        pygame.draw.line( screen, LINE_COLOR, (3 * SQUARE_SIZE, 0), (3 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
        # 4 vertical
        pygame.draw.line( screen, LINE_COLOR, (4 * SQUARE_SIZE, 0), (4 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
        # 5 vertical
        pygame.draw.line( screen, LINE_COLOR, (5 * SQUARE_SIZE, 0), (5 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
        # 6 vertical
        pygame.draw.line( screen, LINE_COLOR, (6 * SQUARE_SIZE, 0), (6 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
        
    
def draw_figures():
    CIRCLE_RADIUS = SQUARE_SIZE / 2 - CIRCLE_WIDTH
    SPACE = SQUARE_SIZE - CROSS_WIDTH
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE/2 ), int( row * SQUARE_SIZE + SQUARE_SIZE/2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col] == 2:
                pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )	
                pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )

def chooseMatrixGra():
	#borders
	pygame.draw.rect(screen, WHITE, (WIDTH / (WIDTH / 100), HEIGHT / 7 + HEIGHT / 14, WIDTH - (WIDTH / (WIDTH / 100)) * 2, HEIGHT / 7))
	pygame.draw.rect(screen, WHITE, (WIDTH / (WIDTH / 100), ((HEIGHT / 7) *3  + HEIGHT / 14), WIDTH - (WIDTH / (WIDTH / 100)) * 2, HEIGHT / 7))
	pygame.draw.rect(screen, WHITE, (WIDTH / (WIDTH / 100), ((HEIGHT / 7) *5 + HEIGHT / 14), WIDTH - (WIDTH / (WIDTH / 100)) * 2, HEIGHT / 7))
 
	#text
	font = pygame.font.SysFont('cambria', 40)
	text1 = font.render('CHOOSE MATRIX TYPE', True, WHITE)
	text2 = font.render('3x3', True, BLACK)
	text3 = font.render('5x5', True, BLACK)
	text4 = font.render('7x7', True, BLACK)
	screen.blit(text1, (WIDTH / 2 - WIDTH / 3.5, HEIGHT / 14))
	screen.blit(text2, (WIDTH / 2 - WIDTH / 24, HEIGHT / 7 + HEIGHT / 14 + HEIGHT / 28))
	screen.blit(text3, (WIDTH / 2 - WIDTH / 24, (HEIGHT / 7) *3  + HEIGHT / 14 + HEIGHT / 28))
	screen.blit(text4, (WIDTH / 2 - WIDTH / 24, (HEIGHT / 7) *5 + HEIGHT / 14 + HEIGHT / 28))
def choiceOption(choose):
    chooseMatrixGra()
    pygame.display.update()
    while choose == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0] # x
                mouseY = event.pos[1] # y
                if mouseX < WIDTH - (WIDTH / (WIDTH / 100)) and mouseX > (WIDTH / (WIDTH / 100)) and mouseY > HEIGHT / 7 + HEIGHT / 14 and mouseY < (HEIGHT / 7) * 2 + HEIGHT / 14:
                    choose = 1
                elif mouseX < WIDTH - (WIDTH / (WIDTH / 100)) and mouseX > (WIDTH / (WIDTH / 100)) and mouseY > (HEIGHT / 7) * 3 + HEIGHT / 14 and mouseY < (HEIGHT / 7) * 4 + HEIGHT / 14:
                    choose = 2
                elif mouseX < WIDTH - (WIDTH / (WIDTH / 100)) and mouseX > (WIDTH / (WIDTH / 100)) and mouseY > (HEIGHT / 7) * 5 + HEIGHT / 14 and mouseY < (HEIGHT / 7) * 6 + HEIGHT / 14:
                    choose = 3
            if(choose == 1 or choose == 2 or choose == 3):
                break
                break
    return choose
                    
def mark_square(row, col, player):
	board[row][col] = player

def available_square(row, col):
	return board[row][col] == 0

def isBoardFull():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 0:
				return False

	return True

def check_win(player):
	# vertical win check
	ver_board = np.transpose(board)
	returnCol = 0
	for col in ver_board:
		if all(col == player):
			draw_vertical_winning_line(returnCol, player)
			printResult(1,player)
			return 1
		else: 
			returnCol += 1
		

	# horizontal win check
	returnRow = 0
	for row in board:
		if all(row == player):
			draw_horizontal_winning_line(returnRow, player)
			printResult(1,player)
			return 1
		else: 
			returnRow += 1

	# asc diagonal win check
	asc = np.diag(np.flipud(board))
	if all(asc == player):
		draw_asc_diagonal(player)
		printResult(1,player)
		return 1

	# desc diagonal win check
	desc = np.diag(board)
	if all(desc == player):
		draw_desc_diagonal(player)
		printResult(1,player)
		return 1

	#draw
	if isBoardFull():
		printResult(-1,player)
		return -1

	return 0

def draw_vertical_winning_line(col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR
	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

def draw_horizontal_winning_line(row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )
def printResult (check, player):
    if player == 1:
        plr = 'O'
    else:
        plr = 'X'
    font = pygame.font.SysFont('cambria', 60)
    if check == 1:
        win = font.render(plr + ' WIN', True, RED, BLACK)
        screen.blit(win, (WIDTH / 2 - 60, HEIGHT / 2 - 60))
    elif check == -1:
        draw = font.render("DRAW", True, RED, BLACK)
        screen.blit(draw, (WIDTH / 2 - 60, HEIGHT / 2 - 60))
def restart():
	screen.fill( BG_COLOR )
	draw_lines(choose)
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0
   
# ---------
# VARIABLES
# ---------
player = 1
game_over = False

# --------
# CHOICE MENU
# --------

choose = choiceOption(0)
BOARD_ROWS, BOARD_COLS, SQUARE_SIZE = boardRC(choose)
# -------------
# CONSOLE BOARD
# -------------
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

screen.fill(BG_COLOR)
draw_lines(choose)
pygame.display.update()
# --------
# MAINLOOP
# --------
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // SQUARE_SIZE)
			clicked_col = int(mouseX // SQUARE_SIZE)

			if available_square( clicked_row, clicked_col ):
				mark_square( clicked_row, clicked_col, player )
				if check_win( player ) == 1 or check_win( player ) == -1:
					game_over = True		
				player = player % 2 + 1

				draw_figures()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				player = 1
				game_over = False

	pygame.display.update()