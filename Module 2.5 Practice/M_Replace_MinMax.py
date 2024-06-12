

# Read input values
N = int(input().strip())  # Number of elements
A = list(map(int, input().strip().split()))  # List of N numbers
# print(A)
# print(' '.join(map(str, A)))

# # Find indices of the minimum and maximum values
min_index = A.index(min(A))
max_index = A.index(max(A))

# print(min_index
# print(max_index)

# # Swap the minimum and maximum values in the array
A[min_index], A[max_index] = A[max_index], A[min_index]

# # Print the modified array
print(' '.join(map(str, A)))
