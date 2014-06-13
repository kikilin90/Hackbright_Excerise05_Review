def main():
	filename = "twain.txt"
	text = open(filename)

	clean_content = []

	for word in text: # this iterates over the file and check inside
		listtext = word.strip().split() # it breaks the file up into a list of words and characters
		for cleanword in listtext: # this iterates over each word in the list
			if cleanword != "": # this checks for blank spaces
				#cleanword.lower()
				lowercap = cleanword.lower()
				clean_content.append(lowercap)
			else:
				pass

	count = [0]*26
	
	for word in clean_content:
		for character in word:
			char = ord(str(character))
			if char >= 97 and char <= 122:
				count[char - 97] += 1

	for abc in count:
		print abc

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