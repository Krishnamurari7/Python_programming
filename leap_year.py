year = int(input("Enter the year: "))



#single line comment
# if year % 4 == 0:
#     if year % 400 == 0:
#         print("it is leap year")
#     elif year % 100 == 0:
#         print('not a Leap Year')
#     else:
#         print('Leap Year')
# else:
#     print('Not a Leap Year')


"""
Multiline comment
if year % 4 == 0:               
    if year % 400 == 0:
        print("it is leap year")
    elif year % 100 == 0:
        print('not a Leap Year')
    else:
        print('Leap Year')
else:
    print('Not a Leap Year')"""

if year % 4 == 0 and year % 100 != 0:
    print('Leap Year')
elif year % 100 == 0 and year % 400 == 0:
    print('Leap Year')
else:
    print('Not a Leap Year')