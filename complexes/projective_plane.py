#This experiemnt has been designed by Pawel Dlotko, p.t.dlotko@swansea.ac.uk
#It is distributed under GPLv3 licence

import numpy as np
import gudhi as gd
#Create a simplex tree
#Simplices can be inserted one by one
#Vertices are indexed by integers
#Notice that inserting an edge automatically insert its vertices (if they were #not already in the complex)
st = gd.SimplexTree()

st.insert([1,4,8])
st.insert([1,2,8])
st.insert([2,6,8])
st.insert([2,3,6])
st.insert([3,5,6])
st.insert([1,3,5])
st.insert([4,5,9])
st.insert([4,8,9])
st.insert([7,8,9])
st.insert([6,7,8])
st.insert([4,6,7])
st.insert([4,5,6])
st.insert([1,3,5])
st.insert([3,5,9])
st.insert([2,3,9])
st.insert([2,7,9])
st.insert([1,2,7])
st.insert([1,4,7])

L = st.get_filtration() #Get a list with all the simplices

for smplx in L:
	print(smplx)

print("dimension=", st.dimension())

print("num_simplices=", st.num_simplices())
print("num_vertices=", st.num_vertices())
print("Number of 0-simplices=", len(st.get_skeleton(0)) )
print("Number of 1-simplices=", len(st.get_skeleton(1)) - len(st.get_skeleton(0)))
print("Number of 2-simplices=", len(st.get_skeleton(2))-len(st.get_skeleton(1)) )