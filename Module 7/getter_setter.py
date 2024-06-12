class User:
    def __init__(self,name,age,money) -> None:
        self._name=name
        self._age=age
        self.__money=money

    # getter without any setter is readonly attribute
    @property # it is convert to attribute
    def age(self):
        return self._age
    
    # getter
    @property
    def salary(self):
        return self.__money
    
    #setter
    @salary.setter
    def salary(self,value):
        if value<0:
            return self.__money
        self.__money += value


samsu=User('Kopa',21,12000)
# print(samsu.__money)    #can not access without method
# print(samsu.age()) # access by when as a method

print(samsu.age) # access as a attribute
print(samsu.salary)

samsu.salary=4500
print(samsu.salary)