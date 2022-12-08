"""
Tow class example
=================
This example shows how to use the PolyKriging Tow class. The tow class is
designed to handle the parametrization and geometrical analysis of a fiber tow.
A Tow instance is created by passing the surface points of the tow to the
constructor.
"""

import polykriging as pk
import numpy as np

"""Parametrization & Geometrical analysis (vertical cut plane)"""
# Load the surface points of fiber tow
path = pk.example("surface points")
surf_points = pk.pk_load(path).to_numpy()

#####################################################################
# We clip the coordinates to discard the part of the tow that is necessary for
# the modeling of the tow.
mask = (surf_points[:, 0] > 1.1 - 0.2) & (surf_points[:, 0] < 11.55 + 0.2)
surf_points_clip = surf_points[mask]

#####################################################################
# Exchange the first and last column for geometry analysis. Note that
# the last column is deemed as the label column. Namely, the points
# with the same label are considered as belonging to the same slice and
# are parametrized in the radial direction (theta). This data reorder
# is necessary for the users.
coordinates = surf_points_clip[:, [2, 1, 0]]

# # filtering the points
# mask = abs(coordinates[:, -1] - 9.196) > 0.09
# coordinates = coordinates[mask]

""" Utilization of the PolyKriging Tow class """
# Create a Tow instance
tow = pk.Tow(surf_points=coordinates, tex=0, name="binder_4", order="zyx")

# Get the parametric coordinates of the tow: The points on the same slice
# are parametrized in the radial direction (theta) and stored in the
# normalized distance column of the attribute, tow.coordinates, a pandas
# DataFrame.
df_coord = tow.coordinates  # parametric coordinates of the tow

# Get the geometrical features of the tow: The geometrical features of the tow
# are stored in the attribute, tow.geom_features, a pandas DataFrame.
# For straight fiber tows, the geometrical features can be used as an approximation
# of the actual tow geometry. But for wavy tows, such as binder, the geometrical
# features are not accurate enough. We need to redo the geometrical analysis
# after identifying the normal cross-sections of the tow.
df_geom = tow.geom_features  # geometrical features of the tow

################################################################################
# Resampling the control points of the tow with a uniform spacing in the
# normalized distance direction. The resampling is necessary to create a
# parametric representation based on dual kriging.
theta_res = 35  # number of control points in the radial direction
sample_position = np.linspace(0, 1, theta_res, endpoint=True)  # equal spaced points (normalized distance)
pts_krig, expr_krig = tow.krig_cs(krig_config=("lin", "cub"),
                                  skip=2, sample_position=sample_position,
                                  smooth=0.0001)

# tow.save("./tow/binder_4.tow")
# tow = np.load("./tow/binder_4.tow", allow_pickle=True).tolist()

mesh = tow.surf_mesh(plot=True, save_path="./test_data/binder_4.ply", end_closed=True)

trajectory_sm = tow.trajectory(smooth=0.0015, plot=False,
                               save_path="./test_data/trajectory.ply", orientation=True)

# Get the axial lines of the tow (the lines connecting the parametrized control points in
# the axial direction)
line_axi = tow.axial_lines(plot=True)

# Get the radial lines of the tow (the lines connecting the parametrized control points in
# the radial direction)
line_rad = tow.radial_lines(plot=True)

# The returned object clipped will be removed in the future. It is used for debugging.
cross_section, plane, clipped = tow.normal_cross_section(algorithm="pyvista")

df_geom = tow.geom_features