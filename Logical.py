a = 12
b = 34
c = 56
 
 #and Operator check all condition are true equal to true
 #or operator check one condition are true equal to true
 
print(a > b and b > c) #12>34 and 34 > 56 == false
 
print(a < b and b < c) #12<34 and 34<56 == true

print(a == b and b == c) # 12==34 and 34==56  ==false

print(a != b and b != c) # 12 != 34 and 34 != 56 == true

print(a > b or b > c) # 12>34 or 34 > 56 ==false

print(a < b or b < c) # 12<34 or 34 < 56==true

print(a == b or b == c)

print(a != b or b != c)

print(not(a > b or b > c))

print(not(a < b or b < c))

print(not(a == b or b == c))

print(not(a != b or b != c))

print(not(12>56) and 34>12 and not(67<34))


 
 