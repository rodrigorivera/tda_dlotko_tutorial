#This experiemnt has been designed by Pawel Dlotko, p.t.dlotko@swansea.ac.uk
#It is distributed under GPLv3 licence

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import gudhi as gd
import random as rd
import math
rd.seed()
number_of_points = 50
u = 0
dx = 2*math.pi/number_of_points;
xv = []
yv = []
zv = []
c = 5
a = 1
for i in range (0,number_of_points):
	v = 0
	for j in range (0,number_of_points):
		xx = (c+a*math.cos(v))*math.cos(u)
		yy = (c+a*math.cos(v))*math.sin(u)
		zz = a*math.sin(v)
		xv.append( xx )
		yv.append( yy )
		zv.append( zz )
		v = v+dx
	u = u + dx


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xv, yv,zv)
plt.show()


points_ = list( zip(xv,yv,zv) )
rips_complex = gd.RipsComplex(points=points_,max_edge_length=1)
simplex_tree = rips_complex.create_simplex_tree(max_dimension=3)
#optional:
simplex_tree.persistence()
simplex_tree.betti_numbers()