# -*- coding: utf-8 -*-
# Week 10, Homework
# Problem 5
"""
A dislocation in a metal, approaching an obstacle such as a precipitate or
dispersion particle can either cut through the obstacle or be pinned at the
obstacle and bow out around it.

Iron carbide (Fe3C) particles are dispersed in iron. The surface energy of Fe3C
is 2J/m2, the shear modulus of iron is 64GPa and the Burgers vector of iron is
0.25nm. What minimum surface energy of the obstacle is required to induce
dislocations to be pinned at the obstacles and bow out around them?
"""

import numpy as np
pi = np.pi

b = 0.25*1e-9
G = 64.0*1e9
gammaCarb = 2.0

alpha = 0.5

UeL = alpha*G*b**2
print UeL