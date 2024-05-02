year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 400 == 0:
        print("it is leap year")
    elif year % 100 == 0:
        print('not a Leap Year')
    else:
        print('Leap Year')
else:
    print('Not a Leap Year')