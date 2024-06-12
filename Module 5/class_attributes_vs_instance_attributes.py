# class shop:
#     cart=[] #cart is a class attriute
#     def __init__(self,buyer):
#         self.buyer=buyer

#     def add_to_cart(self,item):
#         self.cart.append(item)

# mehzbeeb=shop('meh jabeen')
# mehzbeeb.add_to_cart('shoes')
# mehzbeeb.add_to_cart('phone')

# print(mehzbeeb.cart)

# nisho=shop('noisho')

# nisho.add_to_cart('cap')
# nisho.add_to_cart('watch')
# print(nisho.cart)

# -----------------------------

class shop:
    shopping_mall='jamuna'
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[] #cart is an instant attribute

    def add_to_cart(self,item):
        self.cart.append(item)


mehzbeeb=shop('meh jabeen')
mehzbeeb.add_to_cart('shoes')
mehzbeeb.add_to_cart('phone')

print(mehzbeeb.cart)

nisho=shop('noisho')

nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)