import pygame
import Define


def update(dis):
    display = dis

    display.fill(Define.black)

    for i in range(0, Define.grid_num):
        for j in range(0, Define.grid_num):
            grid_rect_x = Define.left_margin + i * Define.grid_size + (2 * i)
            grid_rect_y = Define.top_margin + j * Define.grid_size + (2 * j)

            pygame.draw.rect(display, Define.white,
                             [grid_rect_x, grid_rect_y, Define.grid_size, Define.grid_size])

    return
