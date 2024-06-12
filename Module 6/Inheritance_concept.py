#Base class, parent class

# class BaseClass:
#     pass

# class DerivedClass(BaseClass):
#     pass

class Vehicle:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price

    def __repr__(self) -> str:
        return f'{self.name} {self.price}'

    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat=seat
        super().__init__(name, price)
    def __repr__(self) -> str:
        return f'{self.price} {self.price}'

    



    


class Truck(Vehicle):
     def __init__(self, name, price,weight) -> None:
          self.weight=weight
          super().__init__(name, price)

class PickUpTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)


class AcBus(Bus):
    def __init__(self, name, price, seat,temperature) -> None:
        self.temperature=temperature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()
    


# """
# 1.Simple inheritance: parent class --> child class( Cadget---->)
# (Gadget -->Laptop)

# 2. Multi level inheritance: Granda---> Parent -->Child (Vehicle)--->
# Bus--->AcBus

# """
