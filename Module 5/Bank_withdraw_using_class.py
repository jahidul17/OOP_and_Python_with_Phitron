
class bank:
    def __init__(self,balance):
        self.balnce=balance
        self.min_withdraw=100
        self.max_withdraw=100000

    def get_balance(self):
        return self.balance
        
    def deposit(self,amount):
        if amount>0:
            self.balnce += amount

    def withdraw(self,amount):
        if amount<self.min_withdraw:
            print(f'You can withdraw below {self.min_withdraw}') 
        elif amount>self.max_withdraw:
            print(f'You can not withdraw more than{self.max_withdraw}') 
        else:
            self.balnce -=amount
            print(f'Here is your money {amount}') 
            print(f'your balance after withdraw{self.balnce}')

# brck = bank(1500)

# brck.withdraw(250)
# brck.withdraw(25000000)

dbbl=bank(5000)
dbbl.deposit(2000)
dbbl.deposit(6000)
print(dbbl.balnce)




