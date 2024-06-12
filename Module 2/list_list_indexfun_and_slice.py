#array means list here

# index= 0  1  2  3  4  5  6  7  8  9
numbers=[45,32,46,78,73,67,89,23,45,38]
#index= -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 

# it has consider 2 way positive and negative index
print(numbers[4],numbers[-3])

# list(start:end)
# start from the start index and stops before the end index
print(numbers[2:6])
print(numbers[-5:-2])


# index= 0  1  2  3  4  5  6  7  8  9
numbers=[45,32,46,78,73,67,89,23,45,38]
#index= -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
# list(start:end:step)

print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[1:7:-1]) # not posible
print(numbers[7:1:-1]) # posible

print(numbers[3:])#by default continue till end
print(numbers[:4])#start form began
print(numbers[:])#start to end or shortcut to copy a list
print(numbers[: : 1])#start to end with step
print(numbers[: : 2])#start to end with step
print(numbers[: : -1])#start to end but reverse with step
print(numbers[: : -2])#start to end but reverse with step
