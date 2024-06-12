#static attribute (Class attribute)
#static method @static method
#class method @class method
#differences between static method and class method

class Shopping:
    cart=[]
    origin='China'

    def __init__(self,name,location) -> None:
        self.name='Zahidul'
        self.location='Jamuna City'

    def purchase(self,item,price,amount):
        remaining=amount-price
        print(f'Buying:{item} for price: {price} and remaning: {remaining}')

    @staticmethod
    def multiply(a,b): #static method can not need self
        return print(a*b)

    @classmethod
    def hudai_dakhi(self,item):
        print('Hudai dekhi kintu kinmu na just ac er hawa khaite aschi ->',item)


basundhara=Shopping('Basu end hara','not popular location')
basundhara.purchase('lungi',480,1000)

# Shopping.purchase(2,3,5) #it can not work for  @classmethod


# basundhara.hudai_dakhi('lungi')
Shopping.hudai_dakhi('shirt') #it work for declear class method

#static method
Shopping.multiply(4,6)
