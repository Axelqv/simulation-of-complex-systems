import numpy as np
from scipy.spatial import Voronoi, ConvexHull
PI = np.pi

def generate_positions(N, L, disp_factor=None):
    positions = np.random.rand(N,2) * L - L/2
    orientations = np.random.rand(N) * 2*PI
    if disp_factor:
        positions[:, 0] = positions[:, 0] + disp_factor
        positions[:, 1] = positions[:, 1] + disp_factor
    positions = particle_boundary(positions, L)
    return [positions, orientations]

def particle_boundary(positions, L):
    for i in range(len(positions)):
        x = positions[i, 0]
        y = positions[i, 1]

        if x < -L/2:
            positions[i, 0] = x + L
        elif x > L/2:
            positions[i, 0] = x - L

        if y < - L/2:
            positions[i, 1] = y + L
        elif y > L/2:
            positions[i, 1] = y - L

    return positions

def particle_within_radius(positions, R):
    particles_with_neighbours = dict()
    nr_of_particles = len(positions)
    for i in range(nr_of_particles):
        list_of_neighbours = []
        for j in range(nr_of_particles):
            if i == j:
                continue
            if np.linalg.norm(positions[i, :] - positions[j, :]) < R:
                list_of_neighbours.append(j)
        particles_with_neighbours[i] = list_of_neighbours
    return particles_with_neighbours


def get_velocities(orientations, v=1):
    N = len(orientations)
    velocities = np.zeros((N, 2))
    for i in range(N):
        theta = orientations[i]
        velocities[i, 0] = v * np.cos(theta)
        velocities[i, 1] = v * np.sin(theta)
    return velocities

def global_alignment(velocities, v=1):
    N = len(velocities)
    sum = np.sum(velocities, axis=0) / v
    global_alignment_fac = np.linalg.norm(sum) / N
    return global_alignment_fac

def polygon_area(vor, particle_index):
    polygon_index = vor.point_region[particle_index]
    index_of_vertices = vor.regions[polygon_index]
    polygon_vertices = vor.vertices[index_of_vertices]
    return ConvexHull(polygon_vertices).volume

def global_clustering(positions, R):
    N = len(positions)
    vor = Voronoi(positions)
    counter = 0
    for i in range(N):
        polygon_index = vor.point_region[i]
        index_of_corners = vor.regions[polygon_index]
        polygon_corners = vor.vertices[index_of_corners]
        area = PolyArea(polygon_corners)
        if area < PI * R**2:
            counter += 1
    clustering_coeff = counter / N
    return clustering_coeff


def PolyArea(corners):
    x = corners[:, 0]
    y = corners[:, 1]
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))



pos, orientations = generate_positions(10, 100, 0.5)
par = particle_within_radius(pos, 2)
velocities = get_velocities(orientations)
alignment_fac = global_alignment(velocities)
cluster_coeff = global_clustering(pos, 1)
print(cluster_coeff)


