a = list(filter(lambda x : x % 2 == 1, range(1, 20)))
print(a)

b = [x ** 2 for x in range (1, 11) if  x % 2 == 1]

print(b)

c = [x for x in [3, 4, 5, 6, 7] if x > 5]

print(c)

d = list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))
print(d)
