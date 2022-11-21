import numpy as np
from scipy.spatial import Voronoi, cKDTree
PI = np.pi


def generate_positions_orientations(N, L, disp_factor=None):
    positions = np.random.rand(N, 2) * L - L/2
    orientations = (np.random.rand(N) - 0.5) * 2*PI
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

def particle_within_radius(positions, R, L):
    # particles_with_neighbours = dict()
    # nr_of_particles = len(positions)
    # for i in range(nr_of_particles):
    #     list_of_neighbours = []
    #     for j in range(nr_of_particles):
    #         distance1 = np.linalg.norm(positions[j, :] - positions[i, :])
    #         positions = particle_boundary(positions, L)
    #         distance2 = np.linalg.norm(positions[j, :] - positions[i, :])
    #         if distance1 < R:
    #             list_of_neighbours.append(j)
    #         if distance2 < R:
    #             list_of_neighbours.append(j)
    #     particles_with_neighbours[i] = list_of_neighbours
    # return particles_with_neighbours
    # tree = cKDTree(positions)
    # index = tree.query_ball_point(positions, r=R)
    # return index
    N = len(positions)
    index_list = []
    for i in range(N):
        x_distance = np.abs(positions[i, 0] - positions[:, 0])
        y_distance = np.abs(positions[i, 1] - positions[:, 1])
        min_x_distance = np.minimum(x_distance, L-x_distance)
        min_y_distance = np.minimum(y_distance, L - y_distance)
        distance = np.sqrt(min_x_distance**2 + min_y_distance**2)
        indexes = np.where(distance < R)
        index_list.append(indexes)
    return index_list

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
    sum = np.sum(velocities, axis=0)
    global_alignment_fac = np.linalg.norm(sum) / (v*N)
    return global_alignment_fac

# def polygon_area(vor, particle_index):
#     polygon_index = vor.point_region[particle_index]
#     index_of_vertices = vor.regions[polygon_index]
#     polygon_vertices = vor.vertices[index_of_vertices]
#     return ConvexHull(polygon_vertices).volume

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


def update_orientations(positions, orientations, eta, delta_t, R, L):
    N = len(orientations)
    W = np.random.uniform(-1/2, 1/2, N)
    particles_with_neighbours = particle_within_radius(positions, R, L)
    new_orientation = np.zeros(N)
    for i in range(N):
        neighbours = particles_with_neighbours[i][0]
        # nr_of_neighbours = len(neighbours)
        neighbours_orientation = orientations[neighbours]
        # orientations_for_average = np.append(neighbours_orientation, orientations[i])
        if len(neighbours_orientation) == 1:
            average_orientation = neighbours_orientation
        else:
            average_orientation = np.arctan(np.mean(np.sin(neighbours_orientation))/np.mean(np.cos(neighbours_orientation)))
        new_orientation[i] = average_orientation + eta * W[i] * delta_t
    return new_orientation

def update_positions(positions, velocities, delta_t, L):
    new_positions = positions + velocities*delta_t
    new_positions = particle_boundary(new_positions, L)
    return new_positions








# pos, orientations = generate_positions_orientations(10, 10, 0.5)
# par = particle_within_radius(pos, 1)
# print(par)
# velocities = get_velocities(orientations)
# alignment_fac = global_alignment(velocities)
# cluster_coeff = global_clustering(pos, 1)
# print(cluster_coeff)
# new_o = update_orientations(pos, orientations, 0.01, 1, 1)


