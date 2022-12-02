import numpy as np
import random


def random_init_withprob(dim, p):
    grid = np.zeros((dim, dim))
    for i in range(len(grid)):
        for j in range(len(grid)):
            random_nr = random.uniform(0, 1)
            if random_nr <= p:
                grid[i][j] = 1
    return grid

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


def spec(dimension):
    grid = np.zeros((dimension, dimension))
    grid[8, 5:7] = 1
    grid[9, 7] = 1
    grid[7, 7] = 1
    grid[8, 8:12] = 1
    grid[9, 12] = 1
    grid[7, 12] = 1
    grid[8, 13:15] = 1
    return grid

