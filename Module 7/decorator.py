import math
import time

# def timer(fun):
#     def inner():
#         print('time started')
#         # print(fun)
#         fun()
#         print('time ended')
#     return inner


# # time()()


# # It is easy way decorator
# @timer #function as a decorator
# def get_factorial():
#     print('factorial starting')

# # ----------------------------------------------------
# # it is difficult way decorator

# # get_factorial()
# # timer(get_factorial) # that is inner function so no output
# timer(get_factorial)() # now it is call function and get output

#---------------------------------------------------------

# def timer(fun):
#     # def inner(n):
#     # def inner(*args):
#     def inner(*args,**kargs):
   
#         print('time started')
#         # print(fun)
#         # fun(n)
#         # fun(*args)
#         fun(*args,**kargs)
#         print('time ended')
#     return inner

# @timer #function as a decorator
# def get_factorial(n):
#     print('factorial starting')
#     result=math.factorial(n)
#     print(f'factorial of {n} is: {result}')

# # get_factorial(5)
# get_factorial(n=10)

# ------------------------------------------------------------


def timer(fun):
    def inner(*args,**kargs):
   
        print('time started')
        start=time.time()
        fun(*args,**kargs)

        print('time ended')
        end=time.time()

        print(f'Total time taken {end-start}')

    return inner

@timer #function as a decorator
def get_factorial(n):
    print('factorial starting')
    result=math.factorial(n)
    print(f'factorial of {n} is: {result}')

get_factorial(900)
