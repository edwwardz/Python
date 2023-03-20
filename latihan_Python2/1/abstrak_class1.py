from abc import ABC,abstractmethod

class Button (ABC):
    def __init__ (self,set_link):
        self.link = set_link

    @abstractmethod
    def click (self):
        pass

class PushButton (Button):
    def click (self):
        print("Go To: {}".format(self.link))

tombol1 = PushButton("www.Youtube.com")
tombol1.click()