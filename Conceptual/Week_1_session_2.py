
# a=10
# b=10
# c=12
#  #Here a and b same position in memory because data
# print(id(a))
# print(id(b))
# print(id(c))

#Replace charecter
# c="Rahim"
# c=list(c)
# c[0]='F'
# c="".join(c)
# print(c)

# #index
# lst=[1,2,3,4,6]
# print(lst[-2])


#remove duplicate by set function
# lst=[2,3,4,2,2,2,5,6,6,6,8,9]
# lst=set(lst)
# lst=list(lst)
# print(lst)


#Reverse
# a='madam'
# print(a==a[::-1])

#Dictonary
# lst=[2,3,4,2,2,2,5,6,6,6,8,9]
# dictt={item:lst.count(item) for item in lst}
# print(dictt)


# #index and value
# lst=[2,3,4,2,2,2,5,6,6,6,8,9]
# for i,j in enumerate(lst):
#     print(i,j)
# #which value is greater than 5 from lst
# value=5
# new_lst=[i for i,j in enumerate(lst) if j>value]
# print(new_lst)

#Dictonary
# dict_1={'rahim':10,'karim':20,'fahim':4}
# print(dict_1.keys())
# print(dict_1.values())
# print(dict_1.items())

#Dictonary update
# dict_1={'rahim':10,'karim':20,'fahim':4}
# dict_1['hamim']=14
# print(dict_1)


#lambda 
# lst=[1,2,3,4,5,6,7,8,9]
# new_lst=[]
# for i in lst:
#     if i%2 ==0:
#         new_lst.append(i)
#then convert function
# def even_val(lst):
#     for i in lst:
#         if i%2 ==0:
#             new_lst.append(i)
#     return new_lst
# result=even_val(lst)
# print(result)
#above function convert to lambda
# result=list(filter(lambda x:x%2==0,lst))
# print(result)


try:
    num1=int(input())
    num2=int(input())
    result=num1/num2
except ValueError:
    print('Invalid value')#it means when data type error or suppose we divided value string
except ZeroDivisionError:
    print("Division by 0 is not posible")
finally:
    print('end of program')



