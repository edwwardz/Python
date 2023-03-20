import numpy as np


a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

aMat = np.zeros((2,3)) # -> 2 = kolom (kebawah), 3 = baris (kesamping)
bMat = np.ones((2,3))


# stacking Matrix
c = np.vstack((a,b)) # -> vstack = vertikal
d = np.hstack((a,b)) # -> hstack = horizontal

Cmat = np.hstack((aMat,bMat))

print(Cmat)
