import pygame
import numpy as np

size1 = [600,600]
screen = pygame.display.set_mode(size1)

title = "co-SHO"
pygame.display.set_caption(title)
clock = pygame.time.Clock()
SB = 0


while SB == 0:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            touch = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            touch = 0


    pygame.display.update()
#pygame.quit()