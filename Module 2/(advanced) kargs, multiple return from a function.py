# def full_name(first,last):
#     name=f'full name is: {first}{last}'
#     return name

# name=full_name(last='islam',first='Zahidul ')
# print(name)

# 2nd way
def famous_name(first,last,*additional):
    # name=f'{last} {first} '
    print(additional)
    # return name
# name= famous_name(first='Taher',last='Ali')
name= famous_name('Taher ','Ali ','Maulana','Mufti')
# print(name)


# 1st way
# def famous(kargs)
# def famous_name(first,last,**additional):
#     # name=f'{last} {first} '
#     # print(additional['title'])
#     print(additional)
#     # return name

# name=famous_name(first='Zahidul',last='Islam',title='Khan',addtitional='Engineer')

# print(name)


# # 2nd way
# # def famous(kargs)
# def famous_name(first,last,**additional):
#     name=f'{last} {first}'
#     for key,value in additional.items():
#         print(key,value)
#     return name

# name=famous_name(first='Zahidul',last='Islam',title='Khan',addtitional='Shaiok')

# print(name)


# # another way
# def a_lot(num1,num2):
#     sum=num1+num2
#     mul=num1*num2
#     dev=num1/num2
#     sub=num1-num2
#     # return [sum,mul,dev,sub] #tupple
#     return sum,mul,dev,sub
# everything=a_lot(100,20)

# print(everything)


