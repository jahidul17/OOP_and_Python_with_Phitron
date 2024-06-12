class Book: #base class
    def __init__(self,name) -> None:
        self.name=name

    def rea(self):
        pass #Thats mean skip

    #Thats use for must you have implement
    def read(self):
        raise NotImplementedError 


class Physics(Book): #Sub class
    def __init__(self, name,lab) -> None:
        self.lab=lab
        super().__init__(name)
    def read(self):
        print('Reading physics vector chapter')

topon=Physics('topon',True) #Thats call instance

print(issubclass(Physics,Book))
print(isinstance(topon,Physics))
print(isinstance(topon,Book))

