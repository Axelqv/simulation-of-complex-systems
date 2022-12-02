import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


def random_init_grid(dimension):
    return np.random.choice([0, 1], (dimension, dimension)) # Creating a random quadratic grid with zeros and ones


def still_life(dimension, option):
    """initialize the grid to a state that will be the same due to the rules of
    game of life. Different still_life initializations are available a-e. """
    grid = np.zeros((dimension, dimension))
    if option == 'a':
        grid[4:6, 4:6] = 1
    elif option == 'b':
        grid[2][3] = 1
        grid[5][3] = 1
        grid[3][2] = 1
        grid[4][2] = 1
        grid[3][4] = 1
        grid[4][4] = 1
    elif option == 'c':
        grid[2][3] = 1
        grid[3][2] = 1
        grid[4][2] = 1
        grid[5][3] = 1
        grid[5][4] = 1
        grid[3][4] = 1
        grid[4][5] = 1

    elif option == 'd':
        grid[8][5] = 1
        grid[7][4] = 1
        grid[7][6] = 1
        grid[6, 5:7] = 1

    elif option == 'e':
        grid[6][5] = 1
        grid[7][4] = 1
        grid[7][6] = 1
        grid[8][5] = 1

    return grid

def oscillators(dimension, option):
    """Initialization of a grid where the state oscillate for the different generations due
    to the rules of game of life. There is three options of states shown below"""
    grid = np.zeros((dimension, dimension))
    if option == 'blinker':
        grid[6:9, 5] = 1
    elif option == 'toad':
        grid[5, 2:5] = 1
        grid[6, 3:6] = 1
    elif option == 'beacon':
        grid[4, 5:7] = 1
        grid[5, 6] = 1
        grid[6, 3] = 1
        grid[7, 3:5] = 1

    return grid

def glider(dimension, option):
    grid = np.zeros((dimension, dimension))
    if option == 1:
        grid[0, 8] = 1
        grid[1, 7] = 1
        grid[2, 7:10] = 1
    elif option == 2:
        grid[7, 0:3] = 1
        grid[8, 2] = 1
        grid[9, 1] = 1
    elif option == 3:
        grid[7, 7:10] = 1
        grid[8, 7] = 1
        grid[9, 8] = 1
    elif option == 4:
        grid[0, 1] = 1
        grid[1, 2] = 1
        grid[2, 0:3] = 1
    return grid



def find_live_neighbours(state, i, j, boundary=False):
    nr_of_ones = 0
    if boundary:
        right_col = state[:, [len(state)-1]]
        pad_state = np.hstack([right_col, state])
        bottom_row = pad_state[len(pad_state) - 1, :]
        pad_state = np.vstack([bottom_row, pad_state])
        left_col = pad_state[:, [1]]
        pad_state = np.hstack([pad_state, left_col])
        top_row = pad_state[1, :]
        pad_state = np.vstack([pad_state, top_row])
        if pad_state[i][j] == 1:
            nr_of_ones += 1
        if pad_state[i][j+1] == 1:
            nr_of_ones += 1
        if pad_state[i][j + 2] == 1:
            nr_of_ones += 1
        if pad_state[i+1][j] == 1:
            nr_of_ones += 1
        if pad_state[i+1][j + 2] == 1:
            nr_of_ones += 1
        if pad_state[i+2][j] == 1:
            nr_of_ones += 1
        if pad_state[i+2][j + 1] == 1:
            nr_of_ones += 1
        if pad_state[i+2][j+2] == 1:
            nr_of_ones += 1
    else:
        pad_state = np.pad(state, [(1, 1), (1, 1)])
        if pad_state[i][j] == 1:
            nr_of_ones += 1
        if pad_state[i][j+1] == 1:
            nr_of_ones += 1
        if pad_state[i][j + 2] == 1:
            nr_of_ones += 1
        if pad_state[i+1][j] == 1:
            nr_of_ones += 1
        if pad_state[i+1][j + 2] == 1:
            nr_of_ones += 1
        if pad_state[i+2][j] == 1:
            nr_of_ones += 1
        if pad_state[i+2][j + 1] == 1:
            nr_of_ones += 1
        if pad_state[i+2][j+2] == 1:
            nr_of_ones += 1

    return nr_of_ones






def next_gen(state):
    dim = len(state)
    new_state = np.zeros((dim, dim))
    for i in range(len(state)):
        for j in range(len(state)):
            cell = state[i][j]
            nr_live_neighbours = find_live_neighbours(state, i, j, boundary=True)
            new_cell = update_cell_modified(nr_live_neighbours, cell)
            new_state[i][j] = new_cell

    return new_state


# def run_game_of_life(generations):
#     state = random_init_grid(5)
#     list_of_states = [state]
#     print(state)
#     for i in range(generations):
#         new_state = next_gen(state)
#         list_of_states.append(new_state)
#         state = new_state
#     return list_of_states
# game = run_game_of_life(20)


# state = random_init_grid(10)
# state = still_life(10, 'e')
# state = oscillators(10, 'beacon')
# state = glider(10, option=4)


# def animate(i):
#     global state
#     if i > 0:
#         state = next_gen(state)
#
#     plt.pcolormesh(state, edgecolors='k', linewidth=2)
#     ax = plt.gca()
#     ax.set_aspect('equal')
#     plt.title(f"Generation {i}")
#
#
#
# fig = plt.figure()
# anim = FuncAnimation(fig, animate, frames=40, interval=10)
# anim.save("game_of_life_glider4.gif", writer=PillowWriter(fps=1))












# fig, ax = plt.subplots()
# grid = random_init_grid()
# mat = ax.matshow(grid)
# ani = animation.FuncAnimation(fig, , interval=50,
#                               save_count=50)
# plt.show()



