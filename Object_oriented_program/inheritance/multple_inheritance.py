class A:
    def method_a(self):
        print("Ini method a")
class B:

    def method_b(self):
        print("This is B")

class C (A,B):
    pass

Objek = C()

Objek.method_a()
Objek.method_b()
