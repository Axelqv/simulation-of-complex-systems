import matplotlib.pyplot as plt
import numpy as np
import vicsek_model_funs as vicsek
from scipy.spatial import Voronoi, voronoi_plot_2d
import time
# Parameters
L = 100
N = 100
v = 1
delta_t = 1
eta = 0.01
iterations = 10000
R = 1

positions, orientations = vicsek.generate_positions_orientations(N, L)
vor = Voronoi(positions)
fig1 = voronoi_plot_2d(vor, show_vertices=False)


# initial_positions = positions
# initial_orientation = orientations



global_alignment_coeffs = np.zeros(iterations)
clustering_coeffs = np.zeros(iterations)
times = np.zeros(iterations)
start_time = time.time()
for i in range(iterations):
    orientations = vicsek.update_orientations(positions, orientations, eta, delta_t, R, L)
    velocities = vicsek.get_velocities(orientations, v)
    global_alignment_coeffs[i] = vicsek.global_alignment(velocities, v)
    positions = vicsek.update_positions(positions, velocities, delta_t, L)
    clustering_coeffs[i] = vicsek.global_clustering(positions, R)
    times[i] = i
print(time.time() - start_time)

vor = Voronoi(positions)
fig2 = voronoi_plot_2d(vor, show_vertices=False)

plt.figure(3)
plt.plot(times, global_alignment_coeffs)
plt.plot(times, clustering_coeffs)
plt.show()