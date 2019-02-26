#This experiemnt has been designed by Pawel Dlotko, p.t.dlotko@swansea.ac.uk
#It is distributed under GPLv3 licence

import numpy as np
import gudhi as gd
import math
#construction of the grid points x, and the values therein, y = sin(x).
arg = np.linspace(0,10*math.pi,1000)
values = np.sin(arg)
#Size of the sliding window:
N = 200;
swe = []
for i in range(0,len(values)-N):
	point = []
	for j in range(0,N):
		point.append( values[i+j] );
	swe.append( point );
#Now we have the point cloud, and we can compute the persistent homology in dimension 1:


rips_complex = gd.RipsComplex(points=swe,max_edge_length=20)
simplex_tree = rips_complex.create_simplex_tree(max_dimension=2)
persistence = simplex_tree.persistence()
pers = simplex_tree.persistence_intervals_in_dimension(1)
plt = gd.plot_persistence_diagram(persistence)
plt.show()