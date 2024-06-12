
class Animal:
    def __init__(self,name) -> None:
        self.name=name

    #parent attribute
    def make_sound(self):
        print('Animal making some sound')
        # print(self.name)
    

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('I can maou')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('I can barking')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    # def make_sound(self):
    #     print('I can beh beh beh')

don=Cat('Real don')
don.make_sound()

shepard=Dog('Local Shephard')
shepard.make_sound()


mess=Goat('L M')
mess.make_sound() #When make sound can not access go to parent class


less = Goat('gora gori')


animals=[don,shepard,mess]
for animal in animals:
    animal.make_sound()
