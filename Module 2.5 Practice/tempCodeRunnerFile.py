n=input()

reversed_n=n[::-1]

remove_zero_from_leading=str(int(reversed_n))

if n==reversed_n:
    print(reversed_n)
    print('YES')
else:
    print(reversed_n)
    print('NO')