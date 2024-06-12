def sum(a,b=40):
    result=a+b
    print(result)
    return result
sum(5)
sum(5,7)

# 1st way
def all_sum(*numbers):
    print(numbers)
 
total=all_sum(45,34,24,34,56,43,53)

# 2nd way
def all_sum(num1,num2,*numbers):
    print(numbers)
    print(num1,num2)

total=all_sum(45,34,24,34,56,43,53)

# 3rd way

def all_sum(num1,num2,*numbers):
    print(numbers)
    sum=0
    for num in numbers:
        print(num)
        sum=sum+num
    return sum  

total=all_sum(45,34,24,34,56,43,53)
print('all sum = ',total)

def double_it(num1):
    print("Inside the Default_parameters_and_args",num1)
    result=num1+10
    return result


