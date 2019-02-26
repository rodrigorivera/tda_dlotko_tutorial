#This experiemnt has been designed by Pawel Dlotko, p.t.dlotko@swansea.ac.uk
#It is distributed under GPLv3 licence

import numpy as np
import matplotlib.pyplot as plt
import gudhi as gd
import random as rd
import math
rd.seed()
magnitude_of_noise = 0.5
number_of_points = 500
x = 0
dx = 2*math.pi/number_of_points;
xv = []
yv = []
for i in range (0,number_of_points):
	xx = math.sin(x)+rd.random()*magnitude_of_noise
	yy = math.cos(x)+rd.random()*magnitude_of_noise
	xv.append( xx )
	yv.append( yy )
	x = x+dx

plt.scatter(xv,yv)
plt.show()

#now we can construct Rips complexes out of those data:
points_ = list( zip(xv,yv) )
rips_complex = gd.RipsComplex(points=points_,max_edge_length=1.5)
simplex_tree = rips_complex.create_simplex_tree(max_dimension=2)
#optional:
simplex_tree.persistence()
simplex_tree.betti_numbers()