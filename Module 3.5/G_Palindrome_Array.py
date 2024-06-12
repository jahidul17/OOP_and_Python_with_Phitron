
# n=int(input())
# for x in range(1,n):
#   if(x%2==0):
#     print(x)  

# list = ["eat", "sleep", "repeat"]

# for i, val in enumerate(list):
#     print (i, val)

# d = dict()

# d['xyz'] = 123
# d['abc'] = 346

# for i in d:
#     print("% s % d" % (i, d[i]))


# fruits = ["apple", "banana", "cherry"]
# colors = ["red", "yellow", "green"]
# for fruit, color in zip(fruits, colors):
#     print(fruit, "is", color)

# number of elements
n = int(input())

# Below line read inputs from user using map() function
a = list(map(int, 
	int (input()).strip().split()))[:n]

print(' '.join(map(a)))


