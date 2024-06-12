from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #enfforce all derived class to have a eat method
    def eat(self):
        print("I need food")

    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.catagory='Monkey'
        self.name=name
        super().__init__()

    def eat(self):
        print('Hey na nana, I am eating banana')
    def move(self):
        print('Hanging on the brancehes')

layka=Monkey('Lucky')
layka.eat()

