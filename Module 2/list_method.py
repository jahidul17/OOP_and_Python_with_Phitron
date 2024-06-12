
numbers=[40,28,24,64,23,64]

numbers.append(100)
print(numbers)

numbers.insert(2,200)
print(numbers)

numbers.remove(64)
print(numbers)

if 200 in numbers:
    numbers.remove(200)
print(numbers)

last=numbers.pop()
print(last,numbers)

print(numbers.index(24))

# print(numbers.index(60)) # not found in list
# or
if 60 in numbers:
    print(numbers.index(60))
else:
    print("Not found")

numbers=[40,28,24,64,23,64]
sorted=numbers.sort()
# print(sorted)# wrong
print(numbers)

numbers.reverse()
print(numbers)