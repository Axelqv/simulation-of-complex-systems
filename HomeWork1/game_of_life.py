import numpy as np

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


def update_cell(nr_live_neighbours, cell, rule):
    """This function update the cell based on the rules"""
    if rule == 1:
        if cell == 0:
            if nr_live_neighbours == 3:
                cell = 1
        elif cell == 1:
            if nr_live_neighbours != 2 and nr_live_neighbours != 3:
                cell = 0
    elif rule == 2:
        if cell == 0:
            if nr_live_neighbours == 2:
                cell = 1
        elif cell == 1:
            if nr_live_neighbours > 7 or nr_live_neighbours < 2:
                cell = 0
    elif rule == 3:
        if cell == 0:
            if nr_live_neighbours == 2:
                cell = 1
        elif cell == 1:
            if nr_live_neighbours < 4 or nr_live_neighbours > 2:
                cell = 0

    elif rule == 4:
        if cell == 0:
            if nr_live_neighbours == 3:
                cell = 1
        elif cell == 1:
            if nr_live_neighbours > 5 or nr_live_neighbours < 2:
                cell = 0

    elif rule == 'extinction1':
        if cell == 0:
            if nr_live_neighbours == 3:
                cell = 1
        elif cell == 1:
            if nr_live_neighbours > 6 or nr_live_neighbours < 4:
                cell = 0

    elif rule == 'stable':
        if cell == 0:
            if nr_live_neighbours == 3:
                cell = 1
        elif cell == 1:
            if nr_live_neighbours > 4 or nr_live_neighbours < 2:
                cell = 0

    elif rule == 'majority':
        if cell == 1:
            if nr_live_neighbours < 4:
                cell = 0
        elif cell == 0:
            if nr_live_neighbours > 4:
                cell = 1

    return cell


def next_gen(state, rule, boundary=False):
    dim = len(state)
    new_state = np.zeros((dim, dim))
    for i in range(len(state)):
        for j in range(len(state)):
            cell = state[i][j]
            nr_live_neighbours = find_live_neighbours(state, i, j, boundary)
            new_cell = update_cell(nr_live_neighbours, cell, rule)
            new_state[i][j] = new_cell

    return new_state




