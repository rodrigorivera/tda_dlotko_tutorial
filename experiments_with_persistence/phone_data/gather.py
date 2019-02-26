#This experiemnt has been designed by Pawel Dlotko, p.t.dlotko@swansea.ac.uk
#It is distributed under GPLv3 licence

import numpy as np
import pandas as pd
import pickle as pickle
import gudhi as gd
from pylab import *
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from IPython.display import Image
from sklearn.neighbors.kde import KernelDensity
import matplotlib


data_pd = pd.read_csv('activities/walk.csv',decimal=".",delimiter=",")
data = data_pd.values

data = np.delete(data, (0), axis=1)
data = np.delete(data, (3), axis=1)

#now we can visualize the data:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#plt.plot(data [:,0],data [:,1],data [:,2] )
ax.scatter(data[:,0],data[:,1],data[:,2] )
plt.show()

#And now we can compute persistent homology of the data and compare (visually at the moment) different activities.


Rips_complex_sample = gd.RipsComplex(points = data,max_edge_length=0.6 )
Rips_simplex_tree_sample = Rips_complex_sample.create_simplex_tree(max_dimension=2)

diag_Rips = Rips_simplex_tree_sample.persistence()
#diag_Rips
#diag_Rips_0 = Rips_simplex_tree_sample.persistence_intervals_in_dimension(0)
plt = gd.plot_persistence_diagram(diag_Rips)
plt.show()