import numpy as np
import matplotlib.pyplot as plt

def create_input_automaton(cols,generations):
    # input = np.random.randint(2, size=cols)
    input = np.zeros((generations, cols), dtype=np.int8)
    input[0, cols // 2] = 1
    return input


def update_automaton(automaton, rule):
    powers_of_2 = np.array([[4], [2], [1]])
    rule_set = np.binary_repr(rule, width=8)
    rule_set = np.array([int(x) for x in rule_set], dtype=np.int8)
    automaton_shift_right = np.roll(automaton, 1)
    automaton_shift_left = np.roll(automaton, -1)
    stack_matrix = np.vstack((automaton_shift_right, automaton, automaton_shift_left)).astype(np.int8)
    index_matrix = np.sum(powers_of_2 * stack_matrix, axis=0).astype(np.int8)
    new_automaton = rule_set[7 - index_matrix]
    return new_automaton





# def run_cad1(rule,generations, automaton_size):
#     input_automaton = create_input_automaton(automaton_size)
#     new_automaton = input_automaton
#     cell_automata = np.zeros([generations, automaton_size])
#     for i in range(generations):
#         new_automaton = update_automaton(new_automaton, rule)
#         cell_automata[i, :] = new_automaton
#     return cell_automata

def run_cad1(rule,generations, automaton_size):
    cell_automata = create_input_automaton(automaton_size, generations)
    for i in range(generations-1):
        cell_automata[i + 1, :] = update_automaton(cell_automata[i, :], rule)
    return cell_automata




rule = 184
generations = 63
automaton_size = 100

x = run_cad1(rule, generations, automaton_size)



fig = plt.figure(figsize=(10, 10))

ax = plt.axes()
ax.set_axis_off()

ax.imshow(x, interpolation='none',cmap='RdPu')
plt.savefig('elementary_cellular_automaton2.png', dpi=300, bbox_inches='tight')
