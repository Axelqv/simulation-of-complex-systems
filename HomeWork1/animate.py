import game_of_life as gof
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from init_states import glider, random_init_grid, random_init_withprob, oscillators, spec, still_life
from excercise46 import random_config_center

## Different initial states to choose from, just uncomment or write a new one
# state = random_config_center(10)
# state = random_init_grid(10)
# state = still_life(10, 'b')
# state = oscillators(10, '')
state = glider(10, option=1)

# vote_prob = 0.45
# state = random_init_withprob(100, vote_prob)
# state = spec(20)
def animate(i):
    global state
    if i > 0:
        state = gof.next_gen(state, 1, boundary=False)

    plt.pcolormesh(state, edgecolors='k', linewidth=0.01)
    # plt.pcolormesh(state)
    ax = plt.gca()
    ax.set_aspect('equal')
    plt.title(f"Generation {i}")



fig = plt.figure()
anim = FuncAnimation(fig, animate, frames=20, interval=10)
anim.save("new.gif", writer=PillowWriter(fps=2))

