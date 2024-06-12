class Shop:
    products=[]

    def __init__(self,name) -> None:#constractor
        self.name=name
    
    def __repr__(self) -> str:
        return f'This shop now is:{self.name}'
    
    def add_product(self,name,price):
        product=Product(name,price)
        self.products.append(product)



class Product:
    def __init__(self) -> None:
        pass


shop1=Shop("Test Shop")
print(shop1)

