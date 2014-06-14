from sys import argv

def main():
	# begin program

	# getting the argument from the terminal & assigning it to variables
	script, filename = argv
	# opening the filename object
	text = open(filename)
	# creating an empty list
	clean_content = []
	# iterating over the file and check inside
	for word in text:
		# it iterates each line in the file
		# using the .strip() and .split() breaks them up into a list
		listtext = word.strip().split()
		# it iterates over each value in the list
		for cleanword in listtext:
			# checks for blank spaces
			if cleanword != "":
				# lower-capitalize each word
				lowercap = cleanword.lower()
				# appends to the empty list
				clean_content.append(lowercap)
			else:
				pass # do nothing
	# creating a count array for the alphabet containing 26 letters
	count = [0]*26
	# iterating over each word in the clean_content list
	for word in clean_content:
		# goes right into iterating each letter
		# of the word the first for loop iterates over
		for character in word:
			# convert the character from string
			# to ascii code between 97 and 122
			# remember it's always a string
			char = ord(character)
			# using if statement to check for ascii code
			if char >= 97 and char <= 122:
				# add the value of 1 to the count array,
				# depending on their ascii code
				count[char - 97] += 1
	# using iteration to print out the count array
	for abc in count:
		print abc

	# end program

if __name__ == '__main__':
	main()


"""
# This is another faster way to do it.

from sys import argv

def main():

	filename = argv[1]

	input_file = open(filename)
	file_contents = input_file.read()

	counter = [0]*26

	for character in file_contents:
		if ord(str(character)) >= 65 and ord(str(character)) <= 90:
			counter[ord(character.lower()) - 97] += 1
		elif ord(str(character)) >= 97 and ord(character) <= 122:
			counter[ord(character) - 97] += 1
		else:
			pass

	for count in counter:
		print count

if __name__ == "__main__":
	main()
"""