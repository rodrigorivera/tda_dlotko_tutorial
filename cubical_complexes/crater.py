#This example was taken from Bertrand Michel's tutorial available in here:
#http://bertrand.michel.perso.math.cnrs.fr/Enseignements/TDA-Gudhi-Python.html
#Please acknowledge the original source when using it.

import numpy as np
import pandas as pd
import pickle as pickle
import gudhi as gd
from pylab import *
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from IPython.display import Image
from sklearn.neighbors.kde import KernelDensity

f = open("crater_tuto")
#For python 3
#crater = pickle.load(f,encoding='latin1')
#For python 2
crater = pickle.load(f)
f.close()

plt.scatter(crater[:,0],crater[:,1],s=0.1)
plt.show()

#create 10 by 10 cubical complex:
xval = np.arange(0,10,0.05)
yval = np.arange(0,10,0.05)
nx = len(xval)
ny = len(yval)


#Now we compute the values of the kernel density estimator on the center of each point of our grid.
#The values will be stored in the array scores.
kde  =  KernelDensity(kernel='gaussian',  bandwidth=0.3).fit(crater)
positions = np.array([[u,v] for u in xval for v in yval ])
scores =  -np.exp(kde.score_samples(X= positions))

#And subsequently construct a cubical complex based on the scores.
cc_density_crater= gd.CubicalComplex(dimensions= [nx ,ny],top_dimensional_cells = scores)
# OPTIONAL
pers_density_crater  =cc_density_crater.persistence()
plt = gd.plot_persistence_diagram(pers_density_crater).show()