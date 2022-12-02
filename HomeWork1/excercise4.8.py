import game_of_life as gof
from init_states import random_init_grid
import random
import numpy as np
import matplotlib as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def random_init_withprob(dim, p):
    grid = np.zeros((dim, dim))
    for i in range(len(grid)):
        for j in range(len(grid)):
            random_nr = random.uniform(0, 1)
            if random_nr <= p:
                grid[i][j] = 1
    return grid


state = random_init_withprob(100, 0.45)

def animate(i):
    global state
    if i > 0:
        state = gof.next_gen(state, 'majority')

    plt.pcolormesh(state, edgecolors='k', linewidth=2)
    ax = plt.gca()
    ax.set_aspect('equal')
    plt.title(f"Generation {i}")



fig = plt.figure()
anim = FuncAnimation(fig, animate, frames=100, interval=10)
anim.save("majority.gif", writer=PillowWriter(fps=2))



