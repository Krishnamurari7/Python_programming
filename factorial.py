number = int(input("Enter any number:- "))

fact = 1
if number < 0:
    print('Factorial of negative numbers is not defined.')
for i in range(1,number+1):
    fact = fact*i
print(fact)