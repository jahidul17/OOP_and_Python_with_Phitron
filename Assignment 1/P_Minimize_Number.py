n=int(input())

array=list(map(int,input().split()))

count=0
flag=True

while flag is True:
    for i,a in enumerate(array):
        if a%2==1:
            flag=False
            break
        else:
            array[i]=array[i]/2
          
            
    if flag is True:
        count=count+1
        
print(count)

# ----------------------


# n = int(input())
# arr = [int(i) for i in input().split(" ")]


# flag = True
# count = 0

# while flag is True:
#     for i, num in enumerate(arr):
#         # print(f'{i} and {num}')
#         if num % 2 == 1:
#             flag = False
#             break
#         else:
#             arr[i] /= 2
    
#     if flag: count += 1
    
# print(count)

# --------------------------

# def max_operations(N, A):
#     operations = 0
#     while all(a % 2 == 0 for a in A):
#         A = [a // 2 for a in A]
#         operations += 1
#     return operations

# # Reading input
# N = int(input())
# A = list(map(int, input().split()))

# # Printing the result
# print(max_operations(N, A))

