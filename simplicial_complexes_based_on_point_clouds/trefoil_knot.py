#This experiemnt has been designed by Pawel Dlotko, p.t.dlotko@swansea.ac.uk
#It is distributed under GPLv3 licence

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import gudhi as gd
import math
number_of_points = 500
x = 0
dx = 2*math.pi/number_of_points;
xv = []
yv = []
zv = []
for i in range (0,number_of_points):
	xv.append( math.sin(x)+2*math.sin(2*x) )
	yv.append( math.cos(x)-2*math.cos( 2*x ) )
	zv.append( -math.sin(3*x) )
	x = x+dx

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xv, yv,zv)
plt.show()