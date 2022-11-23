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
iterations = 1000
R = 20
# H = np.arange(26)
H = [-4, -8, -16]




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
mean_clusterings = []
mean_alignments = []
clustering_coeffs_list = []
aligment_coeffs_list = []
for h in H:
    positions_list = []
    old_orientations = []
    positions = np.load('initial_positions_8.8.npy')
    orientations = np.load('initial_orientations_8.8.npy')
    old_orientations = [orientations]
    velocities = vicsek.get_velocities(orientations, v)
    positions_list = [positions]
    for i in trange(iterations):
        if i > h > 0:
            global_alignment_coeffs[i] = vicsek.global_alignment(velocities, v)
            clustering_coeffs[i] = vicsek.global_clustering(positions, R, L)
            orientations = vicsek.update_orientations(positions_list[i-h], old_orientations[i-h], eta, delta_t, R, L)
            velocities = vicsek.get_velocities(old_orientations[i-h], v)
            positions = vicsek.update_positions(positions, velocities, delta_t, L)

        else:
            global_alignment_coeffs[i] = vicsek.global_alignment(velocities, v)
            clustering_coeffs[i] = vicsek.global_clustering(positions, R, L)
            orientations = vicsek.update_orientations(positions, orientations, eta, delta_t, R, L)
            velocities = vicsek.get_velocities(orientations, v)
            positions = vicsek.update_positions(positions, velocities, delta_t, L)

        if h == 0:
            clustering_coeffs_list.append(clustering_coeffs)
            aligment_coeffs_list.append(global_alignment_coeffs)

        elif h == 2:
            clustering_coeffs_list.append(clustering_coeffs)
            aligment_coeffs_list.append(global_alignment_coeffs)

        elif h == 25:
            clustering_coeffs_list.append(clustering_coeffs)
            aligment_coeffs_list.append(global_alignment_coeffs)


        old_orientations.append(orientations)
        positions_list.append(positions)


        if i == 999:
            positions_1000.append(positions)
        if i == 9999:
            positions_10000.append(positions)

    mean_clustering = np.mean(clustering_coeffs)
    mean_alignment = np.mean(global_alignment_coeffs)
    mean_clusterings.append(mean_clustering)
    mean_alignments.append(mean_alignment)


# 10 000
# vor = Voronoi(positions_10000[0])
# fig5 = voronoi_plot_2d(vor, show_vertices=False)
# plt.xlim([-L / 2, L / 2])
# plt.ylim([-L / 2, L / 2])
# plt.title(f'Configuration after {10000} iterations. R={R}, noise={eta}, N={N}, h={0}')
#
# vor = Voronoi(positions_10000[2])
# fig5 = voronoi_plot_2d(vor, show_vertices=False)
# plt.xlim([-L / 2, L / 2])
# plt.ylim([-L / 2, L / 2])
# plt.title(f'Configuration after {10000} iterations. R={R}, noise={eta}, N={N}, h={0}')
#
# vor = Voronoi(positions_10000[25])
# fig5 = voronoi_plot_2d(vor, show_vertices=False)
# plt.xlim([-L / 2, L / 2])
# plt.ylim([-L / 2, L / 2])
# plt.title(f'Configuration after {10000} iterations. R={R}, noise={eta}, N={N}, h={0}')

# 1000
vor = Voronoi(positions_1000[0])
fig5 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L / 2, L / 2])
plt.ylim([-L / 2, L / 2])
plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}, h={0}')

vor = Voronoi(positions_1000[2])
fig6 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L / 2, L / 2])
plt.ylim([-L / 2, L / 2])
plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}, h={2}')

# vor = Voronoi(positions_1000[25])
# fig7 = voronoi_plot_2d(vor, show_vertices=False)
# plt.xlim([-L / 2, L / 2])
# plt.ylim([-L / 2, L / 2])
# plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}, h={25}')

# coefficients as function of time
fig1, ax1 = plt.subplots()
ax1.plot(times, aligment_coeffs_list[0], label='Global alignment')
ax1.plot(times, clustering_coeffs_list[0], label='Global clustering')
leg = ax1.legend()
plt.xlabel('t')
plt.ylabel('Clustering coefficient and alignment coefficient')
plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N},h={0}')

fig2, ax2 = plt.subplots()
ax2.plot(times, aligment_coeffs_list[1], label='Global alignment')
ax2.plot(times, clustering_coeffs_list[1], label='Global clustering')
leg = ax2.legend()
plt.xlabel('t')
plt.ylabel('Clustering coefficient and alignment coefficient')
plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N},h={2}')

fig3, ax3 = plt.subplots()
ax3.plot(times, aligment_coeffs_list[2], label='Global alignment')
ax3.plot(times, clustering_coeffs_list[2], label='Global clustering')
leg = ax3.legend()
plt.xlabel('t')
plt.ylabel('Clustering coefficient and alignment coefficient')
plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N},h={25}')


# coefficients as fun of h
fig, ax = plt.subplots()
ax.scatter(H, mean_alignments, label='Global alignment')
ax.scatter(H, mean_clusterings, label='Global clustering')
leg = ax.legend()
plt.xlabel('h')
plt.ylabel('Clustering coefficient and alignment coefficient')
plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N}')
plt.show()
