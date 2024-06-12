
class Product:
    def __init__(self,name,price,quantity) -> None:
        self.name=name
        self.price=price
        self.quantity=quantity


class Shop:
    def __init__(self) -> None:
        self.products=[]

    def add_product(self,product):
        self.products.append(product)





    