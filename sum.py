#sum of two numbers
def sum(a, b):
    print("The value of a is: ", a)
    print("The value of b is: ", b)
    result = a + b
    print("The sum is: ", result)
    return result

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
sum_of_two_numbers = sum(num1, num2)
print(sum_of_two_numbers)
    