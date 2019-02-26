#This experiemnt has been designed by Pawel Dlotko, p.t.dlotko@swansea.ac.uk
#It is distributed under GPLv3 licence

import numpy as np
import gudhi as gd
#Create a simplex tree
#Simplices can be inserted one by one
#Vertices are indexed by integers
#Notice that inserting an edge automatically insert its vertices (if they were
#not already in the complex)
st = gd.SimplexTree()
st.insert([0,2,4],0)
st.insert([0,3,4],0)
st.insert([1,2,4],0)
st.insert([1,3,4],0)
L = st.get_filtration() #Get a list with all the simplices

for smplx in L:
	print(smplx)

print("dimension=", st.dimension())

print("num_simplices=", st.num_simplices())
print("num_vertices=", st.num_vertices())
print("Here is the complex: ", st.get_skeleton(2))