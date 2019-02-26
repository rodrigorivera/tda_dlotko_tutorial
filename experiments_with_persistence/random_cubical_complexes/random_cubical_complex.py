#This experiemnt has been designed by Pawel Dlotko, p.t.dlotko@swansea.ac.uk
#It is distributed under GPLv3 licence

import matplotlib.pyplot as plt
import numpy as np
import random as rd
from mpl_toolkits.mplot3d import Axes3D
import csv
from sklearn import decomposition
import math
import gudhi as gd
from PIL import Image

#in this example we are considering two dimensional complexes
N = 100

#this is where you set the probability:
p = 0.6

bitmap = []
for i in range(0,N*N):
	x = rd.uniform(0, 1)
	if ( x < p ): bitmap.append(1)
	else: bitmap.append(0)

bcc = gd.CubicalComplex(top_dimensional_cells = bitmap, dimensions=[N,N])
diag = bcc.persistence()
#now we can check how many generators in dimension 0 and in dimension 1 we have:
dim0 = bcc.persistence_intervals_in_dimension(0)
dim1 = bcc.persistence_intervals_in_dimension(1)

print "Here is the first Betti number: ", len(dim0)
print "Here is the second Betti number: ", len(dim1)