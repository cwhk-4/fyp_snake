import Define
import Input


class PlayerData:
    def __init__(self):
        self.x = 6
        self.y = 7
        self.dir_x = 0
        self.dir_y = 0
        self.length = 1
        self.game_over = False


player_data = PlayerData()


def start():
    global player_data
    player_data.__init__()


def update():
    global player_data

    # input
    player_data.dir_x, player_data.dir_y, debug_game_over = Input.update(player_data.dir_x, player_data.dir_y)

    # player move
    player_data.x += player_data.dir_x
    player_data.y += player_data.dir_y

    # check game over
    player_data.game_over = check_game_over(player_data.x, player_data.y)

    return player_data.game_over or debug_game_over


def check_game_over(player_x, player_y):
    x = player_x
    y = player_y
    flag = False

    if x >= Define.grid_num:
        flag = True

    if x < 0:
        flag = True

    if y >= Define.grid_num:
        flag = True

    if y < 0:
        flag = True

    return flag


def get_player_x():
    global player_data
    return player_data.x


def get_player_y():
    global player_data
    return player_data.y

