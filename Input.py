import pygame
import Define


def update(dir_x, dir_y):
    x = dir_x
    y = dir_y
    game_over = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if x != 1:
                    x = -1
                    y = 0
            if event.key == pygame.K_d:
                if x != -1:
                    x = 1
                    y = 0
            if event.key == pygame.K_w:
                if y != 1:
                    y = -1
                    x = 0
            if event.key == pygame.K_s:
                if y != -1:
                    y = 1
                    x = 0

            # test quit
            if event.key == pygame.K_ESCAPE:
                game_over = True

    return x, y, game_over
