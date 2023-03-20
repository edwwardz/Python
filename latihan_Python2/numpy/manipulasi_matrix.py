import numpy as np

a = np.array((
            [1,2,3],
            [4,5,6],
            ))
print("Matrix a dengan ukuran:",a.shape)
print(a)

# Transpose matrix -> baris dijadikan kolom (beurutan dengan yang dibawahnya)
print("Transpose Matrix dari a:")
print(a.transpose())
print(np.transpose(a))
print(a.T)

# flattern array, vector baris
print('flatten matrix a')
print(a.ravel())
print(np.ravel(a))

#reshape matrix -> berurutan
print("Reshape matrix a")
print(a.reshape(3,2))

#resize matrix -> merubah sebuah variabel secara permanen 
print("Resize matrix a:")
a.resize(3,2)
print(a)
print("Matrix a dengan ukuran:",a.shape)


