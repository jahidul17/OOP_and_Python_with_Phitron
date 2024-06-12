#There are many design patterns.So learn about.

#Singleton ---> one single instance
#If you want a new instance, you will get the 
#old one (already created) instance

class Singleton:
    __instance=None
    def __init__(self) -> None:
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('This is Singleton. Already have an instance, use that one by one by calling get_instance method')

    @staticmethod   
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
    
first = Singleton.get_instance()
second=Singleton.get_instance()
#Both are same memory location
print(first)
print(second)

last =Singleton() # call raise exception

