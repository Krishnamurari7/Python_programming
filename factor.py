number = int(input("Enter any Number:-"))

for i in range(1,number+1):
    if number%i == 0:
        
        # print(i)
        print(f"{number} is factor of {i}")