import os
import sys
from math import cos, sin
import matplotlib.pyplot as plt

import os
file_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_directory)


def polToCart(polar_coord_r, polar_coord_theta):
    """Convert lists of polar coordinates in lists of cartesian coordinates

    Args:
        polar_coord_r (list): List of polar coordinates r
        polar_coord_theta (list): List of polar coordinates theta

    Returns:
        list: List of cartesian coordinates x
        list: List of cartesian coordinates y
    """
    cart_coord_x = []
    cart_coord_y = []
    for i in range(len(polar_coord_r)):
        r, theta = polar_coord_r[i], polar_coord_theta[i]
        cart_coord_x.append(r * cos(theta))
        cart_coord_y.append(r * sin(theta))
    return cart_coord_x, cart_coord_y


polar_coord_r = []
polar_coord_theta = []
cart_coord_x = []
cart_coord_y = []

with open("earth_trajectory_output.txt") as file:
    for line in file:
        r, theta = line.split(',')
        polar_coord_r.append(float(r))
        polar_coord_theta.append(float(theta))

# plt.plot(range(1024), polar_coord_r)
# plt.show()

cart_coord_x, cart_coord_y = polToCart(polar_coord_r, polar_coord_theta)

print("Nb points =", len(cart_coord_x))
print(cart_coord_x[:5], "\n", cart_coord_y[:5])

margin = 1000
# plt.scatter(cart_coord_x, cart_coord_y)
# plt.scatter(cart_coord_x[0], cart_coord_y[0])
# plt.scatter(cart_coord_x[1023], cart_coord_y[1023])
plt.plot(cart_coord_x, cart_coord_y, "--", color="green", label="Earth Trajectory")
plt.scatter([0], [0], color="red")
plt.xlim(min(cart_coord_x)-margin, max(cart_coord_x)+margin)
plt.ylim(min(cart_coord_y)-margin, max(cart_coord_y)+margin)
plt.legend(loc="lower right")
plt.savefig("../report/img/earth_trajectory_test.png")
plt.show()
