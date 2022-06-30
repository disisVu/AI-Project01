from operator import truediv
import pygame

# Init pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("TicTacToe")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Screen background
    screen.fill((0, 255, 255))
    pygame.display.update()