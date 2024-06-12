# def double_decker():
#     print('starting the double decker')
#     def inner_fun():
#         print('Inside the inner')
#         return 300
#     return inner_fun

# # print(double_decker()) #can not print because inner function
# print(double_decker()()) #now can print

# -------------------------------------------
# def do_something(work):
#     print('work started')
#     print(work)
#     print('work ended')

# do_something(2)
# do_something('ami busy')

# -------------------------------------------
# def do_something(work):
#     print('work started')
#     work()
#     print('work ended')

# def coding():
#     print('coding in python')

# do_something(coding)

# ---------------------------------------------
def do_something(work):
    print('work started')
    work()
    print('work ended')

def sleeping():
    print('Sleeping and dreaming in python')
do_something(sleeping)





