#This experiemnt has been designed by Pawel Dlotko, p.t.dlotko@swansea.ac.uk
#It is distributed under GPLv3 licence

import numpy as np
import gudhi as gd
import matplotlib
import random as rd

st1 = gd.SimplexTree()
st1.insert([1,4,8],0)
st1.insert([1,2,8],1)
st1.insert([2,6,8],2)
st1.insert([2,3,6],3)
st1.insert([3,4,6],4)
st1.insert([1,3,4],5)
st1.insert([4,5,9],6)
st1.insert([4,8,9],7)
st1.insert([7,8,9],8)
st1.insert([6,7,8],9)
st1.insert([5,6,7],10)
st1.insert([4,5,6],11)
st1.insert([1,2,5],12)
st1.insert([2,5,9],13)
st1.insert([2,3,9],14)
st1.insert([3,7,9],15)
st1.insert([1,3,7],16)
st1.insert([1,5,7],17)

diagram1 = st1.persistence(persistence_dim_max=True)

plt1 = gd.plot_persistence_diagram(diagram1)
plt1.show()

st2 = gd.SimplexTree()
st2.insert([1,4,8],0+rd.random())
st2.insert([1,2,8],1+rd.random())
st2.insert([2,6,8],2+rd.random())
st2.insert([2,3,6],3+rd.random())
st2.insert([3,4,6],4+rd.random())
st2.insert([1,3,4],5+rd.random())
st2.insert([4,5,9],6+rd.random())
st2.insert([4,8,9],7+rd.random())
st2.insert([7,8,9],8+rd.random())
st2.insert([6,7,8],9+rd.random())
st2.insert([5,6,7],10+rd.random())
st2.insert([4,5,6],11+rd.random())
st2.insert([1,2,5],12+rd.random())
st2.insert([2,5,9],13+rd.random())
st2.insert([2,3,9],14+rd.random())
st2.insert([3,7,9],15+rd.random())
st2.insert([1,3,7],16+rd.random())
st2.insert([1,5,7],17+rd.random())

diagram2 = st2.persistence(persistence_dim_max=True)

plt2 = gd.plot_persistence_diagram(diagram2)
plt2.show()

diag = st1.persistence_intervals_in_dimension(1)
diag1 = st2.persistence_intervals_in_dimension(1)
print "The Bottleneck distance is : ",gd.bottleneck_distance(diag,diag1)