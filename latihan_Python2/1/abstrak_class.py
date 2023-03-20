# abstrak class adalah mebuat class dengan sama semua method nya
# class biasa instancenya object 
# class abstrak instancenya class
# class abstrak tidak bisa menjadi object 

# make abstrak class
# abc = abstract base class

from abc import ABC,abstractmethod


class Button (ABC):

    @abstractmethod
    def click (self):
        pass

class PushButton(Button):

    def click (self):
        print("Push butoon click")

class radioButton(Button):
    
    def click (self):
        print("Push butoon click")

tombol1 = PushButton()
tombol2 = radioButton()
tombol1.click()
tombol2.click()























