class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name# public attribute
        self._brance='Banani 11' # protected #It's can not rule but you can use as a private attribute
        self.__balance=initial_deposit # pivate #when __ that mean is private attribute

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance=self.__balance-amount
            return amount
        else:
            return f'Fokira taka nai. Current balance{self.__balance}'

rafsun=Bank('Chooto bro',10000)


# print(rafsun.holder_name)
rafsun.holder_name='Boro vai'
rafsun.deposit(40000)
# print(rafsun.get_balance())
# print(rafsun.holder_name)

# -----------------Tick & Tips
# print(dir(rafsun))
print(rafsun._Bank__balance)


