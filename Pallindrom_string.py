words = input("Enter any words:-")

b = words[-1::-1]   #sliciengg of the string

if words == b:
    print(f"{words} is pallindrom")
else:
    print(f"{words} is not pikindrom")
    