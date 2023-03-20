# learn numpy first

import numpy as np

# make vector -> array biasa
a = np.array([1,2,3,4])

#make vector with range
b = np.arange(1,10,2)

# make linspace # 
c = np.linspace(1,10,5) # -> 1 angka awal, 10 angka akhir, 2 berapa banyak angka yang digunakan untuk mencapai angka akhir

# array multidimensi / matrix 
d = np.array([ (1,2,3,4), (5,6,7,8) ])

#matrix dengan nilai 0
e = np.zeros((2,2))

#matrix dengan nilai 1
f = np.ones((3,3))

# matrix identitas # diagonal
g = np.identity(2)
h = np.eye(3)

#display 
print(h)
