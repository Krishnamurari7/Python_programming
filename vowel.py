letter = input("Enter any letter:- ")

# if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
if letter in "aeiouAEIOU":
    print("The letter is vowel")
else:
    print("The letter is Consonent")