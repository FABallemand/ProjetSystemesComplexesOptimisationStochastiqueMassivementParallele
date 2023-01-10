import os
import sys
from math import cos, sin
import matplotlib.pyplot as plt

import os
file_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_directory)

def polToCart(polar_coord):
    """Convert a list of polar coordinates in two lists of cartesian coordinates

    Args:
        polar_coord (list): List of polar coordinates

    Returns:
        list: List of cartesian coordinates
    """
    x = []
    y = []
    for coord in polar_coord:
        r, theta = coord
        x.append(r * cos(theta))
        y.append(r * sin(theta))
    return x, y

polar_coord = []
cart_coord_x = []
cart_coord_y = []

with open("earth_trajectory_output.txt") as file:
    for line in file:
        r, theta = line.split(',')
        polar_coord.append((float(r), float(theta)))

cart_coord_x, cart_coord_y = polToCart(polar_coord)

plt.plot(cart_coord_x, cart_coord_y)
plt.show()
