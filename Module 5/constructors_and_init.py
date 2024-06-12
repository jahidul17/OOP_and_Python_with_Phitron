class phone:
    manufactured='China'

    #it is constractor
    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price

    def send_sms(self,phone,sms):
        text=f'sending to {phone}{sms}'
        print(text)

my_phone=phone('Kala chan','oop',9800)
print(my_phone.owner,my_phone.brand,my_phone.price)

her_phone=phone('sinha akter','samsung',7700)
print(my_phone.owner,my_phone.brand,my_phone.price)

    