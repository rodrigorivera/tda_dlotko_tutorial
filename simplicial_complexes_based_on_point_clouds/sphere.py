#This experiemnt has been designed by Pawel Dlotko, p.t.dlotko@swansea.ac.uk
#It is distributed under GPLv3 licence

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import gudhi as gd
import random as rd
import math
rd.seed()
dimension = 3
number_of_points = 500
points_= []
x = []
y = []
z = []
for i in range (0,number_of_points):
	xx = np.random.rand(dimension)
	xx = 2*xx-1
	sum_=np.sum( xx*xx )
	xx /= math.sqrt(sum_)
	points_.append( xx.tolist() )


rips_complex = gd.RipsComplex(points=points_,max_edge_length=1)
simplex_tree = rips_complex.create_simplex_tree(max_dimension=2)
#optional
simplex_tree.persistence()
simplex_tree.betti_numbers()