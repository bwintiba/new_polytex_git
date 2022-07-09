# ！/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sympy as sym
from polykriging.mdKrig import buildKriging, interp

dataset = [[1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, -1, 0], [0, 0, 1]]
dataset = np.array(dataset)
xy = dataset[:, :2]
z = dataset[:, 2]

expr = buildKriging(xy, z, 'lin', 'cub', nugg=0.001)

zInterp = interp(dataset[:, :2], expr)