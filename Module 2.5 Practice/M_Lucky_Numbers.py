
# it solved chatgptAi

def is_lucky(number):
    # Check if all digits in the number are either 4 or 7
    return all(digit in '47' for digit in str(number))

def find_lucky_numbers(A, B):
    lucky_numbers = []
    for num in range(A, B + 1):
        if is_lucky(num):
            lucky_numbers.append(num)

    if lucky_numbers:
        print(' '.join(map(str, lucky_numbers)))
    else:
        print(-1)

# Read input values
A, B = map(int, input().strip().split())

# Find and print lucky numbers
find_lucky_numbers(A, B)
