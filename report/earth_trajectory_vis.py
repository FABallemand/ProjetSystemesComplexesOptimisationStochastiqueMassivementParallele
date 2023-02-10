import os
import sys
from math import cos, sin, isinf, isnan
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


def createFigureEA(folder, files, title, param):
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
    proba_mut = 0
    var_mut = 0
    nb_gen = 0
    pop_size = 0
    for i in range(len(files)):
        estimated_polar_coord_r = []
        estimated_polar_coord_theta = []
        estimated_cart_coord_x = []
        estimated_cart_coord_y = []
        with open(folder + "/" + files[i] + ".txt") as file:
            k = 0
            if param and i==0:
                firstline = file.readline()
                # print("FIRST LINE =", firstline)
                proba_mut, var_mut, nb_gen, pop_size = firstline.split(",")
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
        x_min = min(min(cart_coord_x), min(estimated_cart_coord_x))
        if isinf(x_min) or isnan(x_min):
            x_min = min(cart_coord_x)
        x_max = max(max(cart_coord_x), max(estimated_cart_coord_x))
        if isinf(x_max) or isnan(x_max):
            x_max = max(cart_coord_x)
        y_min = min(min(cart_coord_y), min(estimated_cart_coord_y))
        if isinf(y_min) or isnan(y_min):
            y_min = min(cart_coord_y)
        y_max = max(max(cart_coord_y), max(estimated_cart_coord_y))
        if isinf(x_max) or isnan(x_max):
            y_max = max(cart_coord_y)
        axs[i].set_xlim(x_min-margin, x_max+margin)
        axs[i].set_ylim(y_min-margin, y_max+margin)
    # Finish figure
    # fig.title(title)
    # fig.legend()
    if param:
        fig.savefig("report/img/" + folder + "_" + proba_mut + "_" + var_mut + "_" + nb_gen + "_" + pop_size + ".png")
    else:
        fig.savefig("report/img/" + folder + ".png")
    # plt.show()


def createFigureGP():
    # Create figure
    fig = plt.figure()
    fig.set_tight_layout(True)
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
    # Found trajectory
    estimated_polar_coord_r = []
    estimated_polar_coord_theta = []
    estimated_cart_coord_x = []
    estimated_cart_coord_y = []
    with open("earth_trajectory_test/earth_trajectory_gp_1_output.txt") as file:
        for line in file:
            r, theta = line.split(',')
            estimated_polar_coord_r.append(float(r))
            estimated_polar_coord_theta.append(float(theta))
    estimated_cart_coord_x, estimated_cart_coord_y = polToCart(estimated_polar_coord_r, estimated_polar_coord_theta)

    # Create figure
    plt.scatter([0], [0], color="red")
    plt.plot(cart_coord_x, cart_coord_y, color="green", label="True trajectory")
    plt.plot(estimated_cart_coord_x, estimated_cart_coord_y, color="orange", label="Estimated trajectory " + str(i))
    x_min = min(min(cart_coord_x), min(estimated_cart_coord_x))
    if isinf(x_min) or isnan(x_min):
        x_min = min(cart_coord_x)
    x_max = max(max(cart_coord_x), max(estimated_cart_coord_x))
    if isinf(x_max) or isnan(x_max):
        x_max = max(cart_coord_x)
    y_min = min(min(cart_coord_y), min(estimated_cart_coord_y))
    if isinf(y_min) or isnan(y_min):
        y_min = min(cart_coord_y)
    y_max = max(max(cart_coord_y), max(estimated_cart_coord_y))
    if isinf(x_max) or isnan(x_max):
        y_max = max(cart_coord_y)
    plt.xlim(x_min-margin, x_max+margin)
    plt.ylim(y_min-margin, y_max+margin)
    # Finish figure
    fig.savefig("report/img/newton_gp_1.png")
    # plt.show()


folder = ["sun_mass", "perihelion_speed", "perihelion_speed_test"]
file = [["trajectory_1", "trajectory_2", "trajectory_3", "trajectory_4"],
    ["trajectory_1", "trajectory_2", "trajectory_3", "trajectory_4"],
    ["trajectory_1", "trajectory_2", "trajectory_3", "trajectory_4"]]
title = ["", "", ""]
param = [False, False, True]

for i in range(len(folder)):
    createFigureEA(folder[i], file[i], title[i], param[i])

createFigureGP()