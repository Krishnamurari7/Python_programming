number = int(input("Enter any number:-"))
digit = 0

while number > 0:
    digit = number % 10
    number = number // 10
    print(digit)
    