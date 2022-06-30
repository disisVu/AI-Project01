from operator import truediv
import pygame

# Init pygame
pygame.init()

# Create screen
scr_width = 800
scr_height = 600
screen = pygame.display.set_mode((scr_width, scr_height))

# Title and Icon
pygame.display.set_caption("TicTacToe")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

playerX_change = 0
playerY_change = 0

# Movement
step = 0.3

def player(x, y):
    screen.blit(playerImg, (x, y))

running = True
while running:

    # Screen background
    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change -= step
            if event.key == pygame.K_DOWN:
                playerY_change += step
            if event.key == pygame.K_LEFT:
                playerX_change -= step
            if event.key == pygame.K_RIGHT:
                playerX_change += step

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_DOWN:
                playerY_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= scr_width - 40:
        playerX = scr_width - 40

    player(playerX, playerY)
    pygame.display.update()