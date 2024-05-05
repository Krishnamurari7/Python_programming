words = input("Enter any words:-")

b = len(words)//2

print(words.lower()[:b] + words.upper()[b:])