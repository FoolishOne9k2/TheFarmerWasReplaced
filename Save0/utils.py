def reset():
    while get_pos_y() != 0:
        move(South)
    while get_pos_x() != 0:
        move(West)

def checker_board(x,y):
    return x % 2 + y % 2 == 0