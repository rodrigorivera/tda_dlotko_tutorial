#This experiemnt has been designed by Pawel Dlotko, p.t.dlotko@swansea.ac.uk
#It is distributed under GPLv3 licence

import numpy as np
import math
import gudhi as gd
from matplotlib import pyplot as plt

N = 100
array = np.zeros((2*N+1,2*N+1))
xExtrem = 2;
yExtrem = 2;

bitmap = []
for i in range(0,2*N+1):
	for j in range (0,2*N+1):
		x = i/(2*float(N)+1)*2*float(xExtrem)-xExtrem
		y = j/(2*float(N)+1)*2*float(xExtrem)-xExtrem
		norm = math.sqrt( x*x + y*y )
		norm =  math.fabs(norm-1)
		array[i][j] = norm
		bitmap.append(norm)


#Here we will display our creation:
plt.imshow(array, cmap='gray', interpolation='nearest', vmin=np.amin(array), vmax=np.amax(array))
#plt.savefig('circle.png')
plt.show()

#Given the input data we can buld a Gudhi btmap cubical complex:
bcc = gd.CubicalComplex(top_dimensional_cells = bitmap, dimensions=[2*N+1,2*N+1])
#optional computation of persistence
#persistence = bcc.persistence()
#plt = gd.plot_persistence_diagram(persistence)
#plt.show()

