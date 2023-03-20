# Diamond problem
# The objek search the class start from inheritance terdekat

class A:
    
    def show(self):
        print('This is show A')

class B(A):
    pass
    #def show(self):
    #    print('This is show B')

class C(A):
    pass
    #def show(self):
    #    print('This is show C')

class D(B,C):
    pass

objek = D()
objek.show()
