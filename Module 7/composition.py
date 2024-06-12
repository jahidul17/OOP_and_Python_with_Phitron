#Know Inheritance vs composition

# Composition involves a "has-a" relationship between objects, 
# while inheritance involves an "is-a" relationship between classes.


#  class Engine:
#     def __init__(self) -> None:
#         pass

#     def start(self):
#         return "Engine started"
    
# class Driver:
#     def __init__(self) -> None:
#         pass

# #car "has a" engine

# class Car:
#     def __init__(self) -> None:
#         self.engine = Engine()
#         self.driver = Driver()

#     def start(self):
#         self.engine.start()

# ----------------------------------------------
# As a computer example
class CPU:
    def __init__(self,cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self,size) -> None:
        self.size=size


class HardDrive:
    def __init__(self,capacity) -> None:
        self.capacity=capacity


class Computer:
    def __init__(self,cores,ram_size,hd_capacity) -> None:
        self.cpu=CPU(cores)
        self.ram=RAM(ram_size)
        self.hard_disc=HardDrive(hd_capacity)
        

mac=Computer(8,16,512)
# print(mac.cpu.cores)
# print(mac.ram.size)
# print(mac.hard_disc.capacity)



