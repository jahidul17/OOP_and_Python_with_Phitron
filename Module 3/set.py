
# https://www.geeksforgeeks.org/python-tuple-methods/

#list[]
#tuple-->()
#set{}
#set: unique item collection. No duplicate.
numbers=[12,56,12,98,78]

print(numbers)
numbers_set=set(numbers)
print(numbers_set)#set

numbers_set.add(55)
print(numbers_set)

numbers_set.remove(78)
print(numbers_set)

for item in numbers_set:
    print(item)

if 55 in numbers_set:
    print('Exist')


A={1, 3 ,5}
B={ 1, 2, 3, 4, 5} 

print(A&B) # A union B
print(A|B) # A union B

a = set('abracadabra')
b = set('alacazam')
print(a)                                # unique letters in a

print(a - b )                             # letters in a but not in b

print(a | b )                             # letters in a or b or both

print(a & b)                          # letters in both a and b

print(a ^ b )                             # letters in a or b but not both


