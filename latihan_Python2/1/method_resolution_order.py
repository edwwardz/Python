# method resolution order // multiple inheritance

class A:
    def show(self):
        print("Ini adalah show A")

class B:
    def show(self):
        print("Ini adalah show B")

class C(B,A):
    pass

objek = C()
objek.show()
#help(objek)