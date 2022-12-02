import numpy as np
from init_states import random_init_grid, still_life, oscillators, glider
from game_of_life import next_gen

N = 8

def random_config_center(N):
    board = np.zeros((N * 3, N * 3))
    center_grid = random_init_grid(N)
    center_rows = len(center_grid)
    board_rows = len(board)
    bottom = board_rows // 2 - (center_rows // 2)
    top = board_rows // 2 + (center_rows // 2)
    board[bottom:top, bottom:top] = center_grid
    return board


def translate_config(config, dir):
    s_x = dir[0]
    s_y = dir[1]
    new_config = np.roll(config, s_x, axis=1)
    new_config = np.roll(new_config, s_y, axis=0)
    return new_config


def check_identical(config, new_config, i):
    dirs = np.array([[0, 0],
                     [0, 1],
                     [0, -1],
                     [1, 1],
                     [1, 0],
                     [1, -1],
                     [-1, -1],
                     [-1, 0],
                     [-1, 1]])

    for dir in dirs:
        if np.array_equal(new_config, translate_config(config, dir)):
            print(f'identical with direction{dir}, generation{i+1}')
            return 'identical'

    return print('Not identical')


def run_game_of_life(generations):
    # state = oscillators(10, 'blinker')
    # state = glider(10, 1)
    state = random_config_center(10)
    list_of_states = [state]
    for i in range(generations):
        new_state = next_gen(state, 1)
        list_of_states.append(new_state)
        state = new_state
    return list_of_states


list_of_states = run_game_of_life(100)

state = list_of_states[0]
for i in range(len(list_of_states) - 1):
    new_state = list_of_states[i + 1]
    identical = check_identical(state, new_state, i)
    if identical == 'identical':
        state = new_state

