number = int(input("Enter any number"))

check = number
count = 0

while number > 0:
    digit = number % 10
    count = count * 10 + digit # 0*10+digit
    number = number // 10
    
if check == count:
    print(f"{check} is pallindrom number")
else:
    print(f"{check} is not pallindrom number")