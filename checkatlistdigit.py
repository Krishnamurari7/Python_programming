def checkString(str):

	# initializing flag variable
	flag_l = False
	flag_n = False

	# checking for letter and numbers in
	# given string
	for i in str:

		# if string has letter
		if i.isalpha():
			flag_l = True

		if i.isdigit():
			flag_n = True
	return flag_l and flag_n


# driver code
print(checkString('thishasboth29'))
print(checkString('geeksforgeeks'))
