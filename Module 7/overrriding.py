#Method overloading
class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

    def eat(self):
        print("Vat mangos polau korma")

    def exercise(self):
        raise NotImplementedError #thats means must be override else error


class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team=team
        super().__init__(name, age, height, weight)

    #overide
    def eat(self):
        print('Vegetables')

    def exercise(self): #require NotImplementedError
        print('gymm e poisa diya gham joria')
    
    # + operator overload
    def __add__(self,other):
        return self.age+other.age
    
    # * operator overload
    def __mul__(self,other):
        return self.weight * other.weight
    
    # len overload
    def __len__(self):
        return 769
    
     # > operator overload
    def __gt__(sefl,other):
        return sefl.age>other.age

sakib=Cricketer('Sakib',38,68,91,'BD')
mushi=Cricketer('Musfik',40,65,80,'BD')
# sakib.eat()
sakib.exercise()


#Operator overloading
print(45+78)
print('Sakib'+'Rakib')
print([98,45]+[45,2,4,767,89])

print(sakib+mushi) # from __add__ thats call dunder method
print(sakib * mushi) #from __mul__
print(len(sakib))

print(mushi>sakib)



