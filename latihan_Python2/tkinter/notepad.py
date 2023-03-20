import io

def code_it(self):
    testObject = self.object1.object2 # at this point, program doesn't know that testObject  is a MyClass object yet
    assert isinstance(testObject , io) # now the program knows testObject is a MyClass object
    testObject.do_it() # from this point on, PyCharm will be able to auto-complete when you are working on testObject