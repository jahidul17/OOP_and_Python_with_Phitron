name="Sakib\'s Khan"
name2="Sakib khan"
name3="""
Sakib khan
number one
"""

print(name)
print(name2)
print(name3)

# String is a sequence of characters

for char in name2:
    print(char)


print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])

#mutable means changeable
#immutable means you can not change it


if 'khan' in name2:
    print('Existes')

# https://www.geeksforgeeks.org/python-string-methods/

print(name2.upper())


text = 'geeKs For geEkS'
print(text.capitalize())


string = "GEEKSF oRGEEKS"
print("lowercase string: ", string.casefold())


#initializing a string
my_string = "Apple mahmud"
#using string count() method
char_count = my_string.count('a')
#printing the result
print(char_count)




text = "geeks for geeks."
# returns False
result = text.startswith('ge')
print(result)

