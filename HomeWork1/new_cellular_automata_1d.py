import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


def create_input_automaton(cols, random_init=True):
    if random_init:
        input = np.random.randint(2, size=cols)
    else:
        input = np.zeros(cols)
        input[cols//2] = 1
    return input


def update_automaton(automaton, rule):
    rule_set = np.binary_repr(rule, width=8)
    new_automaton = np.zeros(len(automaton))
    for i in range(len(automaton)):
        left = automaton[i-1]
        center = automaton[i]
        if i < len(automaton) - 1:
            right = automaton[i+1]
        else:
            right = automaton[0]
        new_automaton[i] = update_cell(left, center, right, rule_set)
    return new_automaton

def update_cell(left, center, right, rule_set):
    if (left == 1 and center == 1 and right == 1):
        return rule_set[0]
    if (left == 1 and center == 1 and right == 0):
        return rule_set[1]
    if (left == 1 and center == 0 and right == 1):
        return rule_set[2]
    if (left == 1 and center == 0 and right == 0):
        return rule_set[3]
    if (left == 0 and center == 1 and right == 1):
        return rule_set[4]
    if (left == 0 and center == 1 and right == 0):
        return rule_set[5]
    if (left == 0 and center == 0 and right == 1):
        return rule_set[6]
    if (left == 0 and center == 0 and right == 0):
        return rule_set[7]


def run_cad1(rule,generations, automaton_size, random_init=True):
    input_automaton = create_input_automaton(automaton_size, random_init)
    new_automaton = input_automaton
    cell_automata = np.zeros([generations+1, automaton_size])
    cell_automata[0, :] = input_automaton
    for i in range(generations):
        new_automaton = update_automaton(new_automaton, rule)
        cell_automata[i+1, :] = new_automaton
    return cell_automata

rule = 184
generations = 70
automaton_size = 200

x = run_cad1(rule, generations, automaton_size, random_init=True)

# #### Plotting
# figure = plt.figure(figsize=(10, 10))
# ax = plt.axes()
# ax.set_axis_off()
# ax.imshow(x, interpolation='none',cmap='Blues')
# plt.savefig('cad1rule32_random.png', dpi=300, bbox_inches='tight')


#### Animation
steps_showing = 100  # number of steps to show in the animation window
iterations_pf = 1  # iterations per frame
frames = int(generations // iterations_pf)  # number of frames in the animation
interval = 50  # interval in ms between consecutive frames

figure = plt.figure(figsize=(10, 10))
ax = plt.axes()
ax.set_axis_off()

def animate(i):
    ax.clear()  # clear the plot
    ax.set_axis_off()  # disable axis

    f = np.zeros((steps_showing, automaton_size), dtype=np.int8)  # initialize with all zeros
    upper_boundary = (i + 1) * iterations_pf  # window upper boundary
    lower_boundary = 0 if upper_boundary <= steps_showing else upper_boundary - steps_showing  # window lower bound.
    for t in range(lower_boundary, upper_boundary):  # assign the values
        f[t - lower_boundary, :] = x[t, :]

    img = ax.imshow(f, interpolation='none', cmap='Blues')
    return [img]

anim = FuncAnimation(figure, animate, frames=frames, interval=10, blit=True)
anim.save("cad1_rule184new.gif", writer=PillowWriter(fps=24))

