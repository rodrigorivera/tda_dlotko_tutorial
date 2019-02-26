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
st.insert([3,4,6])
st.insert([1,3,4])
st.insert([4,5,9])
st.insert([4,8,9])
st.insert([7,8,9])
st.insert([6,7,8])
st.insert([5,6,7])
st.insert([4,5,6])
st.insert([1,2,5])
st.insert([2,5,9])
st.insert([2,3,9])
st.insert([3,7,9])
st.insert([1,3,7])
st.insert([1,5,7])

print("dimension=", st.dimension())

print("num_simplices=", st.num_simplices())
print("num_vertices=", st.num_vertices())
print("skeleton[0]=", len(st.get_skeleton(0)))
print("skeleton[1]=", len(st.get_skeleton(1))-len(st.get_skeleton(0)))
print("skeleton[2]=", len(st.get_skeleton(2))-len(st.get_skeleton(1)))

#This is for Betti numbers computations:
#st.persistence(persistence_dim_max=True)
#st.betti_numbers()
