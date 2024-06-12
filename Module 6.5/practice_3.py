
# Encapsulation------------------------------------------------
# #object and instance both are same
# #in class variable means attribute
# class Shop:
#     # products=[] #class attribute it is public
#     def __init__(self,name) -> None:
#         self.name=name
#         self.products=[] #instance attribute it is private
#         # self.balance=500 #public
#         # self._balance=500 #protect
#         self.__balance=500 #private

#     def add_product(self,name,price,quantity):
#         item=Product(name,price,quantity)
#         self.products.append(item)

#     def sell (self,product):
#         self.balance += product.price

#     def get_balance(self):
#         return self.products
    
#     def tax_add(self):
#         return self.__balance*0.10
    
#     def get_balance(self):
#         return self.__balance - self.tax_add()




# class Product:
#     def __init__(self,name,price,quantity) -> None:
#         self.name=name
#         self.price=price
#         self.quantity=quantity

#     def __repr__(self) -> str:
#         return self.name

# shop1=Shop('zahidul')

# shop1.add_product('jag',150,4)
# shop1.add_product('Mag',50,10)
# shop1.add_product('Glass',80,12)

# shop2=Shop('Rakibul')

# shop2.add_product('Mobile',25000,2)
# shop2.add_product('Monitor',25000,3)
# shop2.add_product('Lapto',25000,1)

# # print(shop1.products)

# # print(shop1.balance)
# # shop1.balance=0
# # print(shop1.balance)


# print(shop1.get_balance())





#Inheritance---------------------------
# class Vehicle:
#     def __init__(self,brand,model) -> None:
#         self.brand=brand
#         self.model=model

# class Car(Vehicle):
#     def __init__(self,brand,model,capacity) -> None:
#         super().__init__(brand,model)
#         self.capacity=capacity


# class Bike:
#     def __init__(self,brand,model,milage) -> None:
#         self.brand=brand
#         self.model=model
#         self.milage=milage


# class ElectricalCar(Car):
#     def __init__(self, brand, model, capacity,battery_Capacity) -> None:
#         super().__init__(brand, model, capacity)
#         self.battery_Capacity=battery_Capacity

# # toyta=Car("Toyota","Corolla",'4')
# # print(toyta.capacity)


# tesla=ElectricalCar("Tesla",'x8',7,1000000000)
# print(tesla.battery_Capacity)
    

#Multiple Inheritance-------------------------

class Watch:
    def __init__(self,brand,model) -> None:
        self.brand=brand
        self.model=model
    def display_time(self):
        print("Display time")


class FitnessTracker:
    def __init__(self,price) -> None:
        self.price=price

    def track_step(self):
        print("Tracking Step")

    def track_calories(self):
        print("Tracking Calories")


class SmartWatch(Watch,FitnessTracker):
    def __init__(self, brand, model,price) -> None:
        Watch.__init__(self,brand,model)
        FitnessTracker.__init__(self,price)

apple=SmartWatch("Apple","ultra",10000)
apple.display_time()
apple.track_step()
apple.track_calories()

