import os
import sys
from math import cos, sin
import matplotlib.pyplot as plt

import os
file_directory = os.path.dirname(os.path.realpath(__file__))
print(os.path.dirname(file_directory))
os.chdir(os.path.dirname(file_directory))


def polToCart(estimated_polar_coord_r, estimated_polar_coord_theta):
    """Convert lists of polar coordinates in lists of cartesian coordinates

    Args:
        estimated_polar_coord_r (list): List of polar coordinates r
        estimated_polar_coord_theta (list): List of polar coordinates theta

    Returns:
        list: List of cartesian coordinates x
        list: List of cartesian coordinates y
    """
    estimated_cart_coord_x = []
    estimated_cart_coord_y = []
    for i in range(len(estimated_polar_coord_r)):
        r, theta = estimated_polar_coord_r[i], estimated_polar_coord_theta[i]
        estimated_cart_coord_x.append(r * cos(theta))
        estimated_cart_coord_y.append(r * sin(theta))
    return estimated_cart_coord_x, estimated_cart_coord_y


def createFigure(folder, files, title):

    # Create figure
    fig, axs = plt.subplots(len(files))
    fig.set_tight_layout(True)
    fig.set_size_inches(6, 12)
    # fig.subplots_adjust(hspace=.5)
    margin = 100
    # Real trajectory
    polar_coord_r = []
    polar_coord_theta = []
    cart_coord_x = []
    cart_coord_y = []
    with open("earth_trajectory_test/earth_trajectory_output.txt") as file:
        for line in file:
            r, theta = line.split(',')
            polar_coord_r.append(float(r))
            polar_coord_theta.append(float(theta))
    cart_coord_x, cart_coord_y = polToCart(polar_coord_r, polar_coord_theta)
    # Found trajectories
    for i in range(len(files)):
        estimated_polar_coord_r = []
        estimated_polar_coord_theta = []
        estimated_cart_coord_x = []
        estimated_cart_coord_y = []
        with open(folder + "/" + files[i] + ".txt") as file:
            for line in file:
                r, theta = line.split(',')
                estimated_polar_coord_r.append(float(r))
                estimated_polar_coord_theta.append(float(theta))
        estimated_cart_coord_x, estimated_cart_coord_y = polToCart(estimated_polar_coord_r, estimated_polar_coord_theta)
        if len(estimated_cart_coord_x) == 0 or len(estimated_cart_coord_y) == 0:
            axs[i].text(0.5, 0.5, "EASEA Error", horizontalalignment='center', verticalalignment='center', transform=axs[i].transAxes)
            continue
        # Create sub-figure
        axs[i].scatter([0], [0], color="red")
        axs[i].plot(cart_coord_x, cart_coord_y, color="green", label="True trajectory")
        axs[i].plot(estimated_cart_coord_x, estimated_cart_coord_y, color="orange", label="Estimated trajectory " + str(i))
        # axs[i].legend()
        axs[i].set_xlim(min(min(cart_coord_x), min(estimated_cart_coord_x))-margin, max(max(cart_coord_x), max(estimated_cart_coord_x))+margin)
        axs[i].set_ylim(min(min(cart_coord_y), min(estimated_cart_coord_y))-margin, max(max(cart_coord_y), max(estimated_cart_coord_y))+margin)
    # Finish figure
    # fig.title(title)
    # fig.legend()
    fig.savefig("report/img/" + folder + ".png")
    # plt.show()


folder = ["sun_mass"]
file = [["trajectory_1", "trajectory_2", "trajectory_3", "trajectory_4"]]
title = ["Evolution des trajectoires au fil des générations"]

for i in range(len(folder)):
    createFigure(folder[i], file[i], title[i])