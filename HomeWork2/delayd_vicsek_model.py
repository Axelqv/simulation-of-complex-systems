import matplotlib.pyplot as plt
import numpy as np
import vicsek_model_funs as vicsek
from scipy.spatial import Voronoi, voronoi_plot_2d

# Parameters
L = 1000
N = 100
v = 3
delta_t = 1
eta = 0.4
iterations = 5000
R = 20
H = np.arange(26)

def update_orientations_with_delay(positions, orientations, eta, delta_t, R, L, old_orientations):
    n = len(old_orientations)
    if h >= n:
        return orientations
    N = len(orientations)
    W = np.random.uniform(-1 / 2, 1 / 2, N)
    particles_with_neighbours = vicsek.particle_within_radius(positions, R, L)
    new_orientation = np.zeros(N)
    if h > 0:
        for i in range(N):
            neighbours = particles_with_neighbours[i]
            neighbours_orientation = orientations[neighbours]
            if len(neighbours_orientation) == 1:
                average_orientation = neighbours_orientation
            else:
                tmp = old_orientations[n-h]
                average_orientation = np.arctan(np.mean(np.sin(tmp[neighbours])) / np.mean(np.cos(tmp[neighbours])))
            new_orientation[i] = average_orientation + eta * W[i] * delta_t
    else:
        new_orientation = vicsek.update_orientations(positions, orientations, eta, delta_t, R, L)
    return new_orientation










positions = np.load('initial_positions_8.8.npy')
orientations = np.load('initial_orientations_8.8.npy')

vor = Voronoi(positions)
fig1 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.title(f'Initial configuration. R={R}, noise={eta}, N={N}')



global_alignment_coeffs = np.zeros(iterations)
clustering_coeffs = np.zeros(iterations)
times = np.arange(iterations)
positions_1000 = []
positions_10000 = []
mean_clusterings = []
mean_alignments = []
for h in H:
    old_orientations = []
    positions = np.load('initial_positions_8.8.npy')
    orientations = np.load('initial_orientations_8.8.npy')
    old_orientations = [orientations]
    for i in range(iterations):
        if h < 0:

            orientations = vicsek.update_orientations(positions, orientations, eta, delta_t, R, L)
            velocities = vicsek.get_velocities(orientations, v)
            positions = vicsek.update_positions(positions, velocities, delta_t, L)

        else:
            velocities = vicsek.get_velocities(orientations, v)
            positions = vicsek.update_positions(positions, velocities, delta_t, L)
            orientations = vicsek.update_orientations_with_delay(positions, orientations, eta, delta_t, R, L, old_orientations)

        old_orientations.append(orientations)
        global_alignment_coeffs[i] = vicsek.global_alignment(velocities, v)
        clustering_coeffs[i] = vicsek.global_clustering(positions, R)

        if i == 999:
            positions_1000.append(positions)
        if i == 9999:
            positions_10000.append(positions)

    mean_clustering = np.mean(clustering_coeffs)
    mean_alignment = np.mean(global_alignment_coeffs)
    mean_clusterings.append(mean_clustering)
    mean_alignments.append(mean_alignment)


# vor = Voronoi(positions)
# fig2 = voronoi_plot_2d(vor, show_vertices=False)
# plt.xlim([-L/2, L/2])
# plt.ylim([-L/2, L/2])
# plt.title(f'Configuration after {iterations} iterations. R={R}, noise={eta}, N={N}')

# vor = Voronoi(positions_10)
# fig3 = voronoi_plot_2d(vor, show_vertices=False)
# plt.xlim([-L/2, L/2])
# plt.ylim([-L/2, L/2])
# plt.title(f'Configuration after {10} iterations. R={R}, noise={eta}, N={N}')

vor = Voronoi(positions)
fig4 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {iterations} iterations. R={R}, noise={eta}, N={N}')


vor = Voronoi(positions_1000[0])
fig5 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}, h={0}')

vor = Voronoi(positions_1000[2])
fig6 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}, h={2}')

vor = Voronoi(positions_1000[25])
fig7 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}, h={25}')





#
# fig, ax = plt.subplots()
# ax.plot(times, global_alignment_coeffs, label='Global alignment')
# ax.plot(times, clustering_coeffs, label='Global clustering')
# leg = ax.legend()
# plt.xlabel('t')
# plt.ylabel('Clustering coefficient and alignment coefficient')
# plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N}')
# plt.show()

# fig, ax = plt.subplots()
# ax.plot(H, mean_alignments, label='Global alignment')
# ax.plot(H, mean_clusterings, label='Global clustering')
# leg = ax.legend()
# plt.xlabel('h')
# plt.ylabel('Clustering coefficient and alignment coefficient')
# plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N}')
# plt.show()

fig, ax = plt.subplots()
ax.scatter(H, mean_alignments, label='Global alignment')
ax.scatter(H, mean_clusterings, label='Global clustering')
leg = ax.legend()
plt.xlabel('h')
plt.ylabel('Clustering coefficient and alignment coefficient')
plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N}')
plt.show()









