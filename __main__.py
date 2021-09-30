import pygame
import Define
import Drawer
import Player


def main():
    pygame.init()

    display = pygame.display.set_mode((Define.display_width, Define.display_height))

    clock = pygame.time.Clock()

    speed = 3

    Player.start()

    # main loop
    while not Player.update():
        # display
        Drawer.update(display, Player.get_player_x(), Player.get_player_y())

        clock.tick(speed)

    return


if __name__ == "__main__":
    main()
