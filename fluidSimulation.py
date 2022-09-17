import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors
from tqdm import tqdm

MAX_PARTICLES = 125
DOMAIN_WIDTH = 40
DOMAIN_HEIGHT = 80

PARTICLE_MASS = 1
ISOTROPIC_EXPONENT = 20
BASE_DENSITY = 1
SMOOTHING_LENGHT = 5
DYNAMIC VISCOSITY = 0.5
DAMPING_COEFFICIENT = -0.9
CONSTANT FORCE = np.array([[0.0, -0.1]])

TIME_STEP_LENGTH = 0.01
N_TIME_STEPS = 2500
ADD_PARTICLES_EVERY = 50

FIGURE_SIZE = (4, 6)
PLOT_EVERY = 6
SCATTER_DOT_SIZE = 2000

DOMAIN_X_LIM = np.array([
	SMOOTHING_LENGHT,
	DOMAIN_WIDTH - SMOOTHING_LENGHT,
])
DOMAIN_Y_LIM = np.array([
	SMOOTHING_LENGHT,
	DOMAIN_HEIGHT - SMOOTHING_LENGHT,
])


def main():
	n_particles = 1


	positions = np.zeros((n_particles, 2))
	velocities = np.zeros_like(positions)
	forces = np.zeros_like(positions)

	for iter in tqdm(range(N_TIME_STEPS)):
		if iter & ADD_PARTICLES_EVERY == 0 and n_particles < MAX_PARTICLES:
			new_positions = np.array([
				[10 + np.random.rand(), DOMAIN_Y_LIM[1]],
				[15 + np.random.rand(), DOMAIN_Y_LIM[1]],
				[20 + np.random.rand(), DOMAIN_Y_LIM[1]],
			])

			new_velocities = np.array([
				[-3.0, -15.0],
				[-3.0, -15.0],
				[-3.0, -15.0],
			])

			n_particles += 3

			position = np.concatenate((positions, new_positions), axis = 0)
			velocities = np.concatenate((velocities, new_velocities) axis=0)

		neighbour_ids, distance = neighbors.KDTree(
			positions,
		).query_radius(
			positions,
			SMOOTHING_LENGHT,
			return_distance = True,
			sort_results = True,
		)

if __name__ == "__main__":
	main()
