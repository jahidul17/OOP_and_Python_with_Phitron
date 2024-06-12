
# x = input()

# n = [int(i) for i in input().split(" ")]

# nums = {}
# for num in n:
#     if(num not in nums):
#         nums[num] = 0
    
#     nums[num] += 1
    
# tot = 0

# for key, val in nums.items():
#     if(val > key):
#         tot += val - key
#     elif(val < key): tot += val   
        
# print(tot)
#--------------------------------------

n=int(input())

a=list(map(int,input().split(" ")))

dic={}

for num in a:
    if num not in dic:
        dic[num]=0
    
    dic[num]=dic[num]+1

removes=0

for key,value in dic.items():
    # print(f'{key} {value}')
    if(value>key):
        removes=removes+(value-key)  
    elif(value<key):
        removes=removes+value
    
print(removes)


# ------------------------------------

# from collections import Counter

# def min_removals_to_good_sequence(a):
#     # Step 1: Count the frequencies of each element
#     freq = Counter(a)
    
   

#     # Step 2: Calculate the minimum number of removals
#     removals = 0
#     for x, count in freq.items():
#         if count > x:
#             removals += count - x
#         elif count < x:
#             removals += count
    
#     return removals

# # Reading input
# N = int(input().strip())
# a = list(map(int, input().strip().split()))

# # Calculate and print the result
# print(min_removals_to_good_sequence(a))

