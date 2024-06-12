def multiple():
    return 3,4
print(multiple())

things='pen','book','water bottle','phone'

# print(type(things))
print(things[0])
print(things[-2])
print(things[1:3])


if 'phone' in things:
    print('Exists')

for item in things:
    print(item)

print(len(things))