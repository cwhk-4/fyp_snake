import pygame
import Define
import Background


def update(dis, x, y):
    player_x = x
    player_y = y
    display = dis

    Background.update(display)

    player_rect_x = Define.left_margin + player_x * Define.grid_size + (2 * player_x)
    player_rect_y = Define.top_margin + player_y * Define.grid_size + (2 * player_y)
    pygame.draw.rect(display, Define.blue,
                     [player_rect_x, player_rect_y, Define.grid_size, Define.grid_size])

    pygame.display.update()
