# try:
#     # result=45/0
#     result=45/5
# except:
#     print("When Error Happened")# when false then execute this statement
# finally:
#     print("Finally Happened")#Must execute this statement

# print('Done')

# #Create a file
# https://docs.python.org/3/library/filesys.html
# # 'w'=write,'a'=append,'r'=read
# with open('message.txt','w') as file:
#     file.write('I love you!, PYTHON!')

# with open('message.txt','a') as file:
#     file.write('I love you!, PYTHON!')


with open('message.txt','r') as file:
    txt=file.read()
    print(txt)