"""
Modify the previous program to read a word list (check words.txt) and then print all 
the words in the book that are not in the word list. How many of them are typos? 
How many of them are common words that should be in the word list, and how many of them are really obscure?
"""
from string import punctuation, whitespace

def words_to_compare():
	list_of_words = []
	fin = open('../words.txt')
	for line in fin:
		word = line.strip()
		list_of_words.append(word)
	return list_of_words

def words_in_file():
	set_words = set()
	checked_word = ''
	with open('../book.txt', 'r') as file:
		# go line by line, seperate words in every line, then check for every character
		for line in file:
			for word in line.split():
					for char in word:
						if char in punctuation or char in whitespace or char.isdigit():
							break
						else:
							# a checked word without punctuation or whitespace
							checked_word += char.lower()
					if checked_word != '':
						set_words.add(checked_word)
					# reset checked_word for next word to check
					checked_word = ''

	return set_words

def common_words():
	common_words_counter = 0
	set_of_words = words_in_file()
	compare_word = words_to_compare()

	for word in set_of_words:
		if word in compare_word:
			common_words_counter += 1
			#print word,
	return common_words_counter


def obscure_words():
	obscure_words_counter = 0
	set_of_words = words_in_file()
	compare_word = words_to_compare()

	for word in set_of_words:
		if not word in compare_word:
			obscure_words_counter += 1
			print word,
	return obscure_words_counter


print common_words()
print obscure_words()


