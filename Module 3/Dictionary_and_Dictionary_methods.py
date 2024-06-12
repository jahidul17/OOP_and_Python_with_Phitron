# key value pair 
# dictionary
# object
# hash table
# overlap with set

#{key:value,key:value}
person={'name':'zahidul islam','Address':'Patuakhali','age':'23'}

print(person)
print(person['name'])
print(person.keys())
print(person.values())
print(list(person))

# add
person['language']='python'
print(person)

#print by loop
person={'name':'zahidul islam','Address':'Patuakhali','age':'23'}

for key,val in person.items():
    print(key,val)

# print index and value form list
numbers=[34,45,74,78,86,88]
for i,val in enumerate(numbers):
    print(i,val)
