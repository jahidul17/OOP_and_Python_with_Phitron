
#base class,parent class, common attribute + functionality class
#derived class, child class, uncommon attribute + functionality class

class Gadget:   #here function attribute is common attribute
    def __init__(self,brand,price,color,origin) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.origin=origin

    def run(self):
        return f'Running Laptop: {self.brand}'

class Laptop:
    def __init__(self,memory,ssd) -> None:
        self.memory=memory
        self.ssd=ssd

    def coding(self):
        return f'Learning python and practicing'

class Phone:
    def __init__(self,dual_sim) -> None:
        self.dual_sim=dual_sim

    def phone_call(self,number,text):
        return f'Sending SMS to: {number} with: {text}'
    
class Camera:
    def __init__(self,pixel) -> None:
        self.pixel=pixel
    
    def run(self):
        pass

    def change_lens(self):
        pass

