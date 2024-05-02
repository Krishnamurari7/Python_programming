#145 => 1!+4!+5! = 1+24+120 = 145

number = int(input("enter any number:-"))
count = 0
check = number

while number > 0:
    digit = number%10
    fact = 1
    for i in range(1,digit+1):
        fact = fact*i
    count += fact
    number = number//10
print(count)

if check == count:
    print(f"{check} is strong number")
else:
    print(f"{check} is not strong number")