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


positions = np.load('initial_positions.npy')
orientations = np.load('initial_orientations.npy')
vor = Voronoi(positions)
fig1 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-50, 50])
plt.title(f'Initial configuration. R={R}, noise={eta}, N={N}')



global_alignment_coeffs = np.zeros(iterations)
clustering_coeffs = np.zeros(iterations)
# times = np.zeros(iterations)
times = np.arange(iterations)
start_time = time.time()
for i in range(iterations):
    orientations = vicsek.update_orientations(positions, orientations, eta, delta_t, R, L)
    velocities = vicsek.get_velocities(orientations, v)
    positions = vicsek.update_positions(positions, velocities, delta_t, L)
    global_alignment_coeffs[i] = vicsek.global_alignment(velocities, v)
    clustering_coeffs[i] = vicsek.global_clustering(positions, R)
    # times[i] = i
    if i==9:
        positions_10 = positions
    if i == 99:
        positions_100 = positions
    if i == 999:
        positions_1000 = positions

print(time.time() - start_time)

vor = Voronoi(positions)
fig2 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {iterations} iterations. R={R}, noise={eta}, N={N}')

vor = Voronoi(positions_10)
fig3 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {10} iterations. R={R}, noise={eta}, N={N}')

vor = Voronoi(positions_100)
fig4 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {100} iterations. R={R}, noise={eta}, N={N}')

vor = Voronoi(positions_1000)
fig5 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}')




fig, ax = plt.subplots()
ax.plot(times, global_alignment_coeffs, label='Global alignment')
ax.plot(times, clustering_coeffs, label='Global clustering')
leg = ax.legend()
plt.xlabel('t')
plt.ylabel('Clustering coefficient and alignment coefficient')
plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N}')
plt.show()
