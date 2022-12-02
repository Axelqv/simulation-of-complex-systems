import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


def create_input_automaton(cols):
    # input = np.random.randint(2, size=cols)
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


def run_cad1(rule,generations, automaton_size):
    input_automaton = create_input_automaton(automaton_size)
    new_automaton = input_automaton
    cell_automata = np.zeros([generations+1, automaton_size])
    cell_automata[0, :] = input_automaton
    for i in range(generations):
        new_automaton = update_automaton(new_automaton, rule)
        cell_automata[i+1, :] = new_automaton
    return cell_automata

rule = 30
generations = 200
automaton_size = 100
input_automaton = create_input_automaton(automaton_size)
# x = run_cad1(rule, generations, automaton_size)

# fig = plt.figure(figsize=(10, 10))
#
# ax = plt.axes()
# ax.set_axis_off()
#
# ax.imshow(x, interpolation='none',cmap='RdPu')
# plt.savefig('elementary_cellular_automaton2.png', dpi=300, bbox_inches='tight')

###########################################################################
# animation
# steps_to_show = 100  # number of steps to show in the animation window
# iterations_per_frame = 1  # how many steps to show per frame
# frames = int(generations // iterations_per_frame)  # number of frames in the animation
# interval=50  # interval in ms between consecutive frames
#
# fig = plt.figure(figsize=(10, 10))
# ax = plt.axes()
# ax.set_axis_off()

# def animate(i):
#     ax.clear()  # clear the plot
#     ax.set_axis_off()  # disable axis
#
#     Y = np.zeros((steps_to_show, automaton_size), dtype=np.int8)  # initialize with all zeros
#     upper_boundary = (i + 1) * iterations_per_frame  # window upper boundary
#     lower_boundary = 0 if upper_boundary <= steps_to_show else upper_boundary - steps_to_show  # window lower bound.
#     for t in range(lower_boundary, upper_boundary):  # assign the values
#         Y[t - lower_boundary, :] = x[t, :]
#
#     img = ax.imshow(Y, interpolation='none', cmap='Blues')
#     return [img]
#
#
# # call the animator
# anim = FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)
# anim.save("cad1.gif", writer=PillowWriter(fps=24))

frames = int(generations // 1)
def animate(i):
    global input_automaton
    if i > 0:
        input_automaton = update_automaton(input_automaton, rule)

    plt.pcolormesh(input_automaton, edgecolors='k', linewidth=2)
    ax = plt.gca()
    ax.set_aspect('equal')
    plt.title(f"Generation {i}")



fig = plt.figure()
anim = FuncAnimation(fig, animate, frames=frames, interval=10)
anim.save("cad1_rule30.gif", writer=PillowWriter(fps=2))