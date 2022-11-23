import numpy as np
import vicsek_model_funs as vicsek

L = 1000
N = 100
positions, orientations = vicsek.generate_positions_orientations(N, L)

np.save('initial_positions_8.8', positions)
np.save('initial_orientations_8.8', orientations)

