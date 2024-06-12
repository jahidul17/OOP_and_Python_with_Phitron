balance=3000
# price=300
def buy_things(item,price):
    # print(f'previous balance value',balance+500)
    # balance=5000
    # balance1=balance-price
    # print(f'balance after buying {item}',balance1)

    # balance=balance-price #local variable
    # print(f'balance after buying {item}',balance)

    #you can access global variable without using the global keyword
    # But, If you want to modify a global variable, you have to use the global keyword
    global balance
    balance=balance-price 
    print(f'balance after buying {item}',balance)


buy_things('sunglass',1000)
