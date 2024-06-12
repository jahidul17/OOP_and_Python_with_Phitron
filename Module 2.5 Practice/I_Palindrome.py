
n=input()
# n=input().strip() #strip method remove leading and trailing (spaces, tabs, and newlines)

reversed_n=n[::-1]

remove_zero_from_leading=str(int(reversed_n))

if n==reversed_n:
    print(remove_zero_from_leading)
    print('YES')
else:
    print(remove_zero_from_leading)
    print('NO')



