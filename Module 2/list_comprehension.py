numbers=[45,34,21,37,80,90]
odds=[]

for num in numbers:
    if num%2==1:
        odds.append(num)

print(odds)

# another way and assign new arry from above array

odd_nums=[num for num in numbers if num%2==1]
print(odd_nums)





players=['Sakib','Musfik','liton']
ages=[35,40,37]

age_comb=[]

for player in players:
    print('Player name: ',player)
    for age in ages:
        print(player,age)
        age_comb.append([player,age])


print(age_comb)

# If is unread able so need not use this
age_comb2=[[player,age] for player in players for age in ages]
print(age_comb2)


# previous topic
# ** used for exponentiation

def solve(a, b):
    return a**b
    
result = solve(2, 4)
print(result)

def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

display_person(Name="Amir Khan", Age="45")

