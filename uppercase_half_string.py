words = input("Enter any words:-")

b = len(words)//2

print(words.upper()[:b] + words.lower()[b:])