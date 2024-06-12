# def call():
#     print('Calling someone i dont know')
#     return 'call done'

class Phone:
    color='blue'
    price=19000
    brand='samsung'
    features=['camera','speaker','hammer']

    def call(self):
        print('Calling one person')
       
    #Extra parameter must need to define method. Here self extra parameter.
    def send_sms(self,phone,sms):
        text=f'sending sms to:{phone} and message: {sms}'
        return text
    
my_phone= Phone()
# print(my_phone)
print(my_phone.price)
print(my_phone.brand)
my_phone.call()


result=my_phone.send_sms('45223','Missy, I missed to miss you')
print(result)