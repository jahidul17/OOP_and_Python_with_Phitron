class Student:
    def __init__(self,name,current_class,id) -> None:
        self.name=name
        self.id=id
        self.current_class=current_class
        

    def __repr__(self) -> str:
        return f'Student with name: {self.name},class:{self.current_class},id:{self.id}'
    

class Teacher:
    def __init__(self,name,subject,id) -> None:
        self.name=name
        self.subject=subject
        self.id=id
    
    def __repr__(self) -> str:
        return f'Teacher:{self.name},Subject:{self.subject},Id: {self.id}'




class School:
    def __init__(self,name) -> None:
        self.name=name
        self.teachers=[]
        self.students=[]
    
    def add_teacher(self,name,subject):
        id=len(self.teachers)+101
        teacher=Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee<6500:
            return 'Not enough fee'
        else:
            id=len(self.students)+1
            student=Student(name,'C',id)
            self.students.append(student)
            return f'{name}, is enrolled with id: {id}, extra money {fee-6500}'

    def __repr__(self) -> str:
        print('Welcome to',self.name)
        print('----Our Teachers-----')
        for teacher in self.teachers:
            print(teacher)
        print('-----Our Students------')
        for student in self.students:
            print(student)
        return 'All done for now'


# # alia=Student('Alia Torkari',9, 1)
# # print(alia)

# # ranbeer=Teacher(f'Douran beer','Algorithm',101)
# # print(ranbeer)


phitron=School('Phiton')
phitron.enroll('alia',5300)
phitron.enroll('Aminul',6700)
phitron.enroll('Salma',5700)
phitron.enroll('Rani',9500)


phitron.add_teacher('Tom Cruise','Algorithm')
phitron.add_teacher('Ali Heider','Data Structure')
phitron.add_teacher('Rakib Hossien','Database')

print(phitron)




# quize 4
# class A:
#     def __init__(self, value):
#         value = 3
#         self.value = value

#     def change(self):
#         self.value = 12


# ans = []
# a = A(13)
# ans.append(a.value)
# a.change()
# ans.append(a.value)
# print(ans)

# quize 5
# class Shop:
#     cart = []

#     def __init__(self, buyer):
#         self.buyer = buyer

#     def add_to_cart(self, item):
#         self.cart.append(item)


# p1 = Shop('meh jabeeeen')
# p1.add_to_cart('shoes')
# p1.add_to_cart('phone')


# nisho = Shop('noisho')
# nisho.add_to_cart('cap')
# nisho.add_to_cart('watch')
# print(nisho.cart)


# quize 6
# class Shop:
#     shopping_mall = 'Jamuna'

#     def __init__(self, buyer):
#         self.buyer = buyer
#         self.cart = []

#     def add_to_cart(self, item):
#         self.cart.append(item)


# p1 = Shop('meh jabeeeen')
# p1.add_to_cart('shoes')
# p1.add_to_cart('phone')


# nisho = Shop('noisho')
# nisho.add_to_cart('cap')
# nisho.add_to_cart('watch')
# print(nisho.cart)

# quize 8
# class Phone:
#     price = 12000
#     color = 'blue'
#     brand = 'samsung'

#     def call(self):
#         print('calling one person')

#     def send_sms(self, phone, sms):
#         text = f'Sending SMS to: {phone+5}'
#         return text


# my_phone = Phone()
# result = my_phone.send_sms(41524, 'Missy, I missed to miss you')
# print(result)
