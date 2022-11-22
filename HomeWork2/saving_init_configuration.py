import numpy as np
import vicsek_model_funs as vicsek

L = 100
N = 100
positions, orientations = vicsek.generate_positions_orientations(N, L)

np.save('initial_positions_new', positions)
np.save('initial_orientations_new', orientations)

