# This is the main executable

import numpy as np

angle = 70

print('The angle in radians is: ' + str(np.deg2rad(angle)))


def smaller_angle(angle):
	return angle - 10.0