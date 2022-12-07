import numpy as np
import matplotlib as plt

class Agent:
    def __init__(self, state, lattice):
        self.position = np.random.randint(lattice + 1, size=2)
        self.state = state

    def update_state(self, state):
        self.state = state

    def move(self, dir):
        if dir == 'up':
            movement = [0, 1]
        elif dir == 'down':
            movement = [0, -1]
        elif dir == 'right':
            movement = [1, 0]
        elif dir == 'left':
            movement = [-1, 0]
        else:
            raise TypeError('the move must be either up, down, left or right!')
        self.update_position(movement)


    def update_position(self, movement):
        self.position += movement




