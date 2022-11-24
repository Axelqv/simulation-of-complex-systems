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
eta = 0.1
iterations = 10000
R = 30
# H = np.arange(26)
H = [0, 2, 25]




positions = np.load('initial_positions_8.8d.npy')
orientations = np.load('initial_orientations_8.8d.npy')

vor = Voronoi(positions)
fig1 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L / 2, L / 2])
plt.title(f'Initial configuration. R={R}, noise={eta}, N={N}')


times = np.arange(iterations)
positions_1000 = []
positions_10000 = []
mean_clusterings = []
mean_alignments = []
clustering_coeffs_list = []
aligment_coeffs_list = []
for h in H:
    global_alignment_coeffs = np.zeros(iterations)
    clustering_coeffs = np.zeros(iterations)
    positions_list = []
    old_orientations = []
    positions = np.load('initial_positions_8.8d.npy')
    orientations = np.load('initial_orientations_8.8d.npy')
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
    if h == 0:
        # clustering_coeffs_list.append(clustering_coeffs)
        # aligment_coeffs_list.append(global_alignment_coeffs)
        clustering_coeffs1 = clustering_coeffs
        aligment_coeffs1 = global_alignment_coeffs

    elif h == 2:
        # clustering_coeffs_list.append(clustering_coeffs)
        # aligment_coeffs_list.append(global_alignment_coeffs)
        clustering_coeffs2 = clustering_coeffs
        aligment_coeffs2 = global_alignment_coeffs

    elif h == 25:
        # clustering_coeffs_list.append(clustering_coeffs)
        # aligment_coeffs_list.append(global_alignment_coeffs)
        clustering_coeffs3 = clustering_coeffs
        aligment_coeffs3 = global_alignment_coeffs




# 10 000
# vicsek.plot_vicsek_model(positions_10000[0], L)
# plt.title(f'Configuration after {10000} iterations. R={R}, noise={eta}, N={N}, h={0}')
#
# vicsek.plot_vicsek_model(positions_10000[2], L)
# plt.title(f'Configuration after {10000} iterations. R={R}, noise={eta}, N={N}, h={2}')
#
# vicsek.plot_vicsek_model(positions_10000[25], L)
# plt.title(f'Configuration after {10000} iterations. R={R}, noise={eta}, N={N}, h={25}')

# 1000
vicsek.plot_vicsek_model(positions_1000[0], L)
plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}, h={0}')

vicsek.plot_vicsek_model(positions_1000[1], L)
plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}, h={2}')

vicsek.plot_vicsek_model(positions_1000[2], L)
plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}, h={25}')

# coefficients as function of time
fig1, ax1 = plt.subplots()
ax1.plot(times, aligment_coeffs1, label='Global alignment')
ax1.plot(times, clustering_coeffs1, label='Global clustering')
leg = ax1.legend()
plt.xlabel('t')
plt.ylabel('Clustering coefficient and alignment coefficient')
plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N},h={0}')

fig, ax = plt.subplots()
ax.plot(times, aligment_coeffs2, label='Global alignment')
ax.plot(times, clustering_coeffs2, label='Global clustering')
leg = ax.legend()
plt.xlabel('t')
plt.ylabel('Clustering coefficient and alignment coefficient')
plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N},h={2}')
#
fig, ax = plt.subplots()
ax.plot(times, aligment_coeffs3, label='Global alignment')
ax.plot(times, clustering_coeffs3, label='Global clustering')
leg = ax.legend()
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

