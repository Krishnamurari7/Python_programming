str = input("Enter any string:-")

a = str.split()
print(a)
res = []
for i in a:
    
    x = i[0].upper()+i[1:-1]+i[-1].upper()
    
    print(x)
    res.append(x)
res = " ".join(res)
print("String after:", res)

    