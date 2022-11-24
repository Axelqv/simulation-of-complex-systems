import matplotlib.pyplot as plt
import numpy as np
import vicsek_model_funs as vicsek
from scipy.spatial import Voronoi, voronoi_plot_2d
from tqdm import trange
# Parameters
L = 1000
N = 100
v = 3
delta_t = 1
eta = 0.4
iterations = 10000
R = 20
h = -2




positions = np.load('initial_positions_8.8.npy')
orientations = np.load('initial_orientations_8.8.npy')

vor = Voronoi(positions)
fig1 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L / 2, L / 2])
plt.title(f'Initial configuration. R={R}, noise={eta}, N={N}')

global_alignment_coeffs = np.zeros(iterations)
clustering_coeffs = np.zeros(iterations)
times = np.arange(iterations)
positions_1000 = []
positions_10000 = []
positions = np.load('initial_positions_8.8.npy')
orientations = np.load('initial_orientations_8.8.npy')
velocities = vicsek.get_velocities(orientations, v)
neighbours_index = vicsek.particle_within_radius_V2(positions, R, L)

for i in trange(iterations):

    global_alignment_coeffs[i] = vicsek.global_alignment(velocities, v)
    clustering_coeffs[i] = vicsek.global_clustering(positions, R, L)
    clone_neighbours_index = np.copy(neighbours_index)
    clone_positions = np.copy(positions)
    clone_velocities = np.copy(velocities)

    for j in range(-h):
        clone_neighbours_index = vicsek.particle_within_radius_V2(clone_positions, R, L)
        orientations = vicsek.update_orientations_V2(orientations, clone_neighbours_index, eta, delta_t, R, L)
        clone_velocities = vicsek.get_velocities(orientations, v)
        clone_positions = vicsek.update_positions(clone_positions, clone_velocities, delta_t, L)

    clone_neighbours_index = vicsek.particle_within_radius_V2(clone_positions, R, L)
    orientations = vicsek.update_orientations_V2(orientations, neighbours_index, eta, delta_t, R, L)
    velocities = vicsek.get_velocities(orientations, v)
    positions = vicsek.update_positions(positions, velocities, delta_t, L)


    if i == 999:
        positions_1000.append(positions)
    if i == 9999:
        positions_10000.append(positions)







# 10 000
vicsek.plot_vicsek_model(positions_10000[0], L)
plt.title(f'Configuration after {10000} iterations. R={R}, noise={eta}, N={N}, h={h}')





# 1000
# vicsek.plot_vicsek_model(positions_1000[0], L)
# plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}, h={-2}')





# coefficients as function of time
fig1, ax1 = plt.subplots()
ax1.plot(times, global_alignment_coeffs, label='Global alignment')
ax1.plot(times, clustering_coeffs, label='Global clustering')
leg = ax1.legend()
plt.xlabel('t')
plt.ylabel('Clustering coefficient and alignment coefficient')
plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N},h={h}')
plt.show()


