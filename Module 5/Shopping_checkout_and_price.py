class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]


    def add_to_cart(self,item,price,quantity):
        product={f'item': item, 'price':price,'quantity':quantity}
        self.cart.append(product)

    def remove_item(self,item,price,quantity):
        product={f'item': item, 'price':price,'quantity':quantity}
        self.cart.remove(product)

    def checkout(self,amount):
        total=0
        for item in self.cart:
            # print(item)
            total += item['price']*item['quantity']
        
        if amount<total:
            print(f'Total amount is: {total}')
            print(f'Please provide {total-amount} more')
        else:
            extra=amount-total
            print(f'Total amount is: {total}')
            print(f'Here is your items and extra money: {extra}')
        
    
swapan=Shopping('Alan Swapan')
swapan.add_to_cart('alu',50,7)
swapan.add_to_cart('dim',12,6)
swapan.add_to_cart('rice',70,25)

print(swapan.cart)

# swapan.remove_item('alu',50,7)
# print(swapan.cart)

swapan.checkout(600)
swapan.checkout(3000)
